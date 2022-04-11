
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt
import PyCO2SYS as pyco2

#%% Import the data

#test1 = pd.read_csv('Pyro_sensor/data/sensor_data1.csv')            #lab seawater, pH=7.8 ish /

test2 = pd.read_csv('Pyro_sensor/data/sensor_data2.csv')      # TERS135 RWS sample

test3 = pd.read_csv('Pyro_sensor/data/sensor_data3.csv')    # CRM batch195
test3['datetime'] = pd.to_datetime(test3.Date)   
test3 = test3.drop(columns='Created')


#%% define a function that devides the columns values by 1000 / no need to apply it for test3 as the data is already given in the format we want

def devide(c):
    return c/1000

# test1 = test1.apply(devide, axis=1)
# test1['scan_counts'] = test1['scan_counts']*1000     #we don't need to devide the scan counts by 1000

test2 = test2.apply(devide, axis=1)
test2['scan_counts'] = test2['scan_counts']*1000


#%% calculate the pH for TERS135 and compare the pH

# SAL DIC TA / 34,31 /2098,528 /2287,849/ for temp = 25 degC  pH total=7.846738945112961


pH_TERS = pyco2.sys(par1=2287.849, par1_type = 1, par2=2098.528,          #calculate the pH for T =25 degC
                    par2_type=2, salinity= 34.31, temperature=25)

pH_TERS_T = pyco2.sys(par1=2287.849, par1_type = 1, par2=2098.528,          #calculate the pH for the T of the sensor
                    par2_type=2, salinity= 34.31, temperature =test2.temp_sol)

pH_TERS_T = pd.DataFrame.from_dict(results)

test2['pH_tot'] = pH_TERS_T['pH_total'].copy()

## Plotting

line1 = test2.pH   # sensor pH
line2 = test2.pH_tot  # calculated the pH with TA/DIC/Sal and temperature from the sensor

fig, ax = plt.subplots(dpi=400)
ax.plot(line1, color = 'green', label='sensor')
ax.plot(line2, color = 'red', label='pyco2sys pH')
ax.legend(loc='lower right')
plt.xlabel('scan_counts')
plt.ylabel('pH')
plt.title('TERSL135 sensor vs measured')
plt.axhline(y = 7.846738945112961, c = 'black', label='pH at 25 degC')  # pH of the sample at 25degC
# plt.xlim(0, 19800)

plt.show()

# test2['drift'] = test2['pH']-test2['pH_tot']
# test2['drift'].mean() 

#%% CRM bottle 195   #pH at 25 degC = 7.862987347263012

crm = pyco2.sys(par1=2213.51, par1_type = 1, par2=2024.96, par2_type=2, salinity= 33.485, temperature=25,
                total_silicate = 3.6,total_phosphate = 0.49)


crm_T = pyco2.sys(par1=2213.51, par1_type = 1, par2=2024.96, par2_type=2, 
                  salinity= 33.485, temperature=test3.solution_temperature,total_silicate = 3.6,
                  total_phosphate = 0.49)

# opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
# opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

crm_T = pd.DataFrame.from_dict(results)

test3['pH_tot'] = crm_T['pH_total'].copy()

##
line1 = test3.pH
line2 = test3.pH_tot

fig, ax = plt.subplots(dpi = 400)
ax.plot(line1, color = 'green', label='sensor')
ax.plot(line2, color = 'red', label='pyco2sys pH')
ax.legend(loc='lower right')
plt.xlabel('scan_counts')
plt.ylabel('pH')
plt.title('CRM-195 sensor vs measured')
plt.axhline(y = 7.864322485574625, c = 'black', label='pH at 25 degC')

# plt.xlim(0, 48000)
# plt.ylim(7.86, 8.2)

plt.show()

# test3['drift'] = test3['pH']-test3['pH_tot']
# test3['drift'].mean() 