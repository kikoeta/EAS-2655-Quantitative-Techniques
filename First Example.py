import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# reads the excel file in the current folder (./), then skips the first row for the data since that's an explanation slide
df=pd.read_excel('./ATL_MonMeanTemp_1879_2022.xlsx',skiprows=1)
print(df)

# gets the year
year = df.Year
# month of august
AUG = df.iloc[:,8]
# temp of all months
All_Month = df.iloc[:1:13]
print(All_Month)

# calculate annual mean from all months data
Annual = All_Month.mean(axis=1)
print(Annual.mean())
print(Annual.median())

# let's plot the August temperature as a function of time
# use this to create a figure separate from all others, code goes below and runs until next plot call using plt.figure
AUGTempFunc = plt.figure('August Temperature Function')
plt.plot(year,AUG)
plt.xlabel('Year')
plt.ylabel('Temperature, deg F')

AUGave = AUG.mean()
print(AUGave)
print('The average August temperature in Atlanta is '+str(round(AUGave,2))+' deg F')

HistogramNoLine = plt.figure('August Temperature Histogram')
bins = np.arange(73,88,1)
plt.hist(AUG,bins)
plt.xlabel('Aug temperature, deg F')
plt.ylabel('frequency (occurrence)')

AUGsd=AUG.std()
print('The AUG standard deviation is '+str(AUGsd))

# we must plot this again since it's a new plot thing, idk
HistogramLine = plt.figure('August Temperature Histogram w/ Line')
bins = np.arange(73,88,1)
plt.hist(AUG,bins)
plt.xlabel('Aug temperature, deg F')
plt.ylabel('frequency (occurrence)')

mu=AUGave
sig=AUGsd
x=np.arange(73,88,0.1)
y=144*1*1/np.sqrt(2*np.pi)/sig*np.exp(-(x-mu)**2/(2*sig**2))
plt.plot(x,y)

# let's make a box plot for Aug
BoxPlotAUG = plt.figure('August Box Plot')
plt.boxplot(AUG)
plt.ylabel('Temperature (deg F)')
plt.xlabel('Aug')

# let's make a box plot
BoxPlotAll = plt.figure('All Months Box Plot')
plt.boxplot(All_Month)
plt.ylim(0,100)
plt.ylabel('Temperature (deg F)')
plt.xlabel('Month')


plt.show()