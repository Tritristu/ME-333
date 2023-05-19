import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
pipeDiameter = 0.9*2.54e-2 # m
area = (np.pi/4)*pipeDiameter**2 # m**2


# Reading in data
roundElbow = pd.read_csv('Minor Loss Lab\RoundElbow.csv')
cappedTee = pd.read_csv('Minor Loss Lab\CappedTee.csv')

# Converting to SI units
roundElbow['Position [m]'] = roundElbow['Position [in]']*2.54e-2
roundElbow['Pressure Drop [Pa] (R_e = 15000)'] = 133.322*roundElbow['Pressure Drop [Torr] (R_e = 15000)']
roundElbow['Pressure Drop [Pa] (R_e = 25000)'] = 133.322*roundElbow['Pressure Drop [Torr] (R_e = 25000)']
roundElbow['Pressure Drop [Pa] (R_e = 35000)'] = 133.322*roundElbow['Pressure Drop [Torr] (R_e = 35000)']

cappedTee['Position [m]'] = cappedTee['Position [in]']*2.54e-2
cappedTee['Pressure Drop [Pa] (R_e = 15000)'] = 133.322*cappedTee['Pressure Drop [Torr] (R_e = 15000)']
cappedTee['Pressure Drop [Pa] (R_e = 25000)'] = 133.322*cappedTee['Pressure Drop [Torr] (R_e = 25000)']
cappedTee['Pressure Drop [Pa] (R_e = 35000)'] = 133.322*cappedTee['Pressure Drop [Torr] (R_e = 35000)']

# Plotting
sns.set_theme()


plt.figure(1)
plt.title('Round Elbow Pressure change vs Position')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 15000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 25000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 35000)')
plt.legend(labels=['R_e=15000','R_e=25000','R_e=35000'],loc='lower right')
plt.ylabel('Pressure Drop [Pa]')
# plt.xlim(0,145)
# plt.ylim(0,250)

plt.show()

