
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import xarray as xr
import cmocean
import seaborn as sns
from matplotlib import pyplot as plt
#%%

test1 = pd.read_csv('data/sensor_data1.csv')

test2 = pd.read_csv('Pyro_sensor/data/sensor_data2.csv')

#%% define a function that devides the columns values by 1000

def devide(c):
    return c/1000

test1 = test1.apply(devide, axis=1)
test1['scan_counts'] = test1['scan_counts']*1000


def devide(c):
    return c/1000

test2 = test2.apply(devide, axis=1)
test2['scan_counts'] = test2['scan_counts']*1000


#%% plots for the first test

def plot_df(sensor, x, y, title="", dpi=400):
    '''make plots
    sensor= dataframe of optode
    x = name of the x axis column
    y = name of the y axis column
    '''
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x,y, data=test1, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=x, ylabel=y)
    plt.show()
    plt.style.use('ggplot')
    
plot_df(test1, "scan_counts", "ambient_light")
plot_df(test1, "scan_counts", "pH")
plot_df(test1, "scan_counts", "phase_shift")
plot_df(test1, "scan_counts", "temp_sol")
plot_df(test1, "scan_counts", "temp_device")
plot_df(test1, "scan_counts", "")
plot_df(test1, "scan_counts", "pH")


#%% plots for the 2nd first test

def plot_df(sensor, x, y, title="", dpi=400):
    '''make plots
    sensor= dataframe of optode
    x = name of the x axis column
    y = name of the y axis column
    '''
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x,y, data=test2, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=x, ylabel=y)
    plt.show()
    plt.style.use('ggplot')
    
plot_df(test2, "scan_counts", "ambient_light")
plot_df(test2, "scan_counts", "pH")
plot_df(test2, "scan_counts", "phase_shift")
plot_df(test2, "scan_counts", "temp_sol")
plot_df(test2, "scan_counts", "temp_device")
plot_df(test2, "scan_counts", "pH")

#%%

fig, ax = plt.subplots( figsize=(10,8), sharey=True)
sns.scatterplot(data=sensor, x="signal_intensity", y="phase_shift", s = 100, palette = 'rocket')
ax.set_title('Sensor pH evolution', fontsize=25)
plt.xlabel("Signal intensity", size =25 )
plt.ylabel("phase shift",size =25)
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
# ax.legend( bbox_to_anchor=(1.05, 1.0), markerscale=2,
#            scatterpoints=1, fontsize=15)
plt.style.use('ggplot')

#%%


fig, ax = plt.subplots( figsize=(10,8), sharey=True)
sns.scatterplot(data=sensor, x="phase_shift", y="pH", s = 100, palette = 'rocket')
ax.set_title('Sensor pH evolution', fontsize=25)
plt.xlabel("Scan counts", size =25 )
plt.ylabel("pH",size =25)
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
# ax.legend( bbox_to_anchor=(1.05, 1.0), markerscale=2,
#            scatterpoints=1, fontsize=15)
plt.style.use('seaborn')

#%% pH vs scan counts

def plot_df(sensor, x, y, title="", xlabel='scan_counts', ylabel='pH', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=45) 
    plt.grid(alpha=0.9)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.scan_counts, y=sensor.pH, title='pH evolution')


#%% pH vs sol temp
def plot_df(sensor, x, y, title="", xlabel='temp_sol', ylabel='pH', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=45) 
    plt.grid(alpha=0.9)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.temp_sol, y=sensor.pH, title='pH evolution')


#%% pH vs signal intensity
def plot_df(sensor, x, y, title="", xlabel='Signal intensity', ylabel='pH', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=45) 
    plt.grid(alpha=0.9)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.signal_intensity, y=sensor.pH, title='pH evolution')

#%%
#%% pH vs signal intensity
def plot_df(sensor, x, y, title="", xlabel='Scan_counts', ylabel='signal intensity', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.scan_counts, y=sensor.signal_intensity, title='Signal intensity')


#%% temp sol vs scan counts
def plot_df(sensor, x, y, title="", xlabel='Scan_counts', ylabel='Temperature solution', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.scan_counts, y=sensor.temp_sol, title='temparature solution evolution')


#%% temp device vs scan counts
def plot_df(sensor, x, y, title="", xlabel='Scan_counts', ylabel='Temperature sensor', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.scan_counts, y=sensor.temp_device, title='device temperature evolution')


#%% temp device vs scan counts
def plot_df(sensor, x, y, title="", xlabel='Temperature solution', ylabel='Temperature sensor', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.temp_sol, y=sensor.temp_device, title='Temp sol vs Temp device')


#%% pH vs ambiant light
def plot_df(sensor, x, y, title="", xlabel='phase shift', ylabel='pH', dpi=400):
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x, y, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    plt.style.use('ggplot')
plot_df(sensor, x=sensor.phase_shift, y=sensor.pH, title='pH vs ambiant light')

#%% scan counts vs ambiant light
def plot_df(sensor, x, y, title="", dpi=400):
    '''make plots
    sensor= dataframe of optode
    x = name of the x axis column
    y = name of the y axis column
    '''
    plt.figure(figsize=(8,5), dpi=dpi)
    plt.scatter(x,y, data=sensor, c="xkcd:red pink", s=10) 
    plt.grid(alpha=1)
    plt.gca().set(title=title, xlabel=x, ylabel=y)
    plt.show()
    plt.style.use('ggplot')
    
plot_df(sensor, "scan_counts", "ambient_light")
plot_df(sensor, "scan_counts", "ambient_light")






#%% looping?




columns=['phase_shift','temp_sol','temp_device','signal_intensity','ambiant_light','pressure','humidity','temp_resistance','pH','scan_counts']

for i in columns:
    fig, ax = plt.subplots(1,1 ,figsize=(10,6))
    sns.scatterplot(y=sensor[i][1:],data=sensor.iloc[1:],order=sensor[i][1:].value_counts().index)
    plt.xlabel('',fontsize=20)
    plt.ylabel('')
    








