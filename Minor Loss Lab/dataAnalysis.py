import pandas as pd
import numpy as np
from scipy.stats import linregress
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
pipeDiameter = 0.9*2.54e-2 # m
area = (np.pi/4)*pipeDiameter**2 # m**2
kinematicViscousity = 1.56e-5 #m**2/s

# Flow rate and Velocity from target Reynolds Numbers
velocity15000 = (15000*kinematicViscousity)/pipeDiameter
velocity25000 = (25000*kinematicViscousity)/pipeDiameter
velocity35000 = (35000*kinematicViscousity)/pipeDiameter

volumetricFlux15000 = area*velocity15000
volumetricFlux25000 = area*velocity25000
volumetricFlux35000 = area*velocity35000

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

# Linear Regression
def trendline(data):
    positions = np.concatenate([data['Position [m]'][0:5],data['Position [m]'][7:10]])
    reynolds15000 = np.concatenate([data['Pressure Drop [Pa] (R_e = 15000)'][0:5],data['Pressure Drop [Pa] (R_e = 15000)'][7:10]])
    reynolds25000 = np.concatenate([data['Pressure Drop [Pa] (R_e = 25000)'][0:5],data['Pressure Drop [Pa] (R_e = 25000)'][7:10]])
    reynolds35000 = np.concatenate([data['Pressure Drop [Pa] (R_e = 35000)'][0:5],data['Pressure Drop [Pa] (R_e = 35000)'][7:10]])
    slope1, intercept1, R, P, Err = linregress(positions, reynolds15000)
    slope2, intercept2, R, P, Err = linregress(positions, reynolds25000)
    slope3, intercept3, R, P, Err = linregress(positions, reynolds35000)
    fitLines = [[slope1,intercept1],[slope2,intercept2],[slope3,intercept3]]
    return fitLines

# def trendline(data):
#     slopeBefore15000, interceptBefore15000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 15000)'][0:5])
#     slopeAfter15000, interceptAfter15000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 15000)'][7:10])
#     slopeBefore25000, interceptBefore25000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 25000)'][0:5])
#     slopeAfter25000, interceptAfter25000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 25000)'][7:10])
#     slopeBefore35000, interceptBefore35000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 35000)'][0:5])
#     slopeAfter35000, interceptAfter35000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 35000)'][7:10])
#     fitLines = [[slopeBefore15000,interceptBefore15000,slopeAfter15000,interceptAfter15000],
#                 [slopeBefore25000,interceptBefore25000,slopeAfter25000,interceptAfter25000],
#                 [slopeBefore35000,interceptBefore35000,slopeAfter35000,interceptAfter35000]]
#     return fitLines

roundElbowFits = trendline(roundElbow)
cappedTeeFits = trendline(cappedTee)

# Plotting
sns.set_theme()

plt.figure(1)
plt.title('Round Elbow Pressure Change vs Position')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 15000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 25000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 35000)')
# for lines in roundElbowFits:
#     pressureDropsBefore = lines[0]*roundElbow['Position [m]'] + lines[1]
#     pressureDropsAfter = lines[2]*roundElbow['Position [m]'] + lines[3]
#     plt.plot(roundElbow['Position [m]'],pressureDropsBefore)
#     plt.plot(roundElbow['Position [m]'],pressureDropsAfter)

for lines in roundElbowFits:
    pressureDrops = lines[0]*roundElbow['Position [m]'] + lines[1]
    plt.plot(roundElbow['Position [m]'],pressureDrops)
plt.legend(labels=['R_e=15000','R_e=25000','R_e=35000','Fitted (R_e=15000)','Fitted (R_e=25000)','Fitted (R_e=35000)'],loc='lower right')
plt.ylabel('Pressure Change [Pa]')

plt.figure(2)
plt.title('Capped Tee Pressure Change vs Position')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 15000)')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 25000)')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 35000)')
for lines in cappedTeeFits:
    pressureDrops = lines[0]*cappedTee['Position [m]'] + lines[1]
    plt.plot(cappedTee['Position [m]'],pressureDrops)
plt.legend(labels=['R_e=15000','R_e=25000','R_e=35000','Fitted (R_e=15000)','Fitted (R_e=25000)','Fitted (R_e=35000)'],loc='lower right')
plt.ylabel('Pressure Change [Pa]')

plt.show()