import pandas as pd
import numpy as np
from scipy.stats import linregress
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
pipeDiameter = 0.9*2.54e-2 # m
area = (np.pi/4)*pipeDiameter**2 # m**2
kinematicViscousity = 1.56e-5 #m**2/s
density = 1.18 # kg/m**3

# Flow rate and Velocity from target Reynolds Numbers
velocity15000 = (15000*kinematicViscousity)/pipeDiameter
velocity25000 = (25000*kinematicViscousity)/pipeDiameter
velocity35000 = (35000*kinematicViscousity)/pipeDiameter
velocities = [velocity15000,velocity25000,velocity35000]

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
    slopeAfter15000, interceptAfter15000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 15000)'][0:5])
    slopeBefore15000, interceptBefore15000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 15000)'][7:10])
    slopeAfter25000, interceptAfter25000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 25000)'][0:5])
    slopeBefore25000, interceptBefore25000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 25000)'][7:10])
    slopeAfter35000, interceptAfter35000, R, P, Err = linregress(data['Position [m]'][0:5], data['Pressure Drop [Pa] (R_e = 35000)'][0:5])
    slopeBefore35000, interceptBefore35000, R, P, Err = linregress(data['Position [m]'][7:10], data['Pressure Drop [Pa] (R_e = 35000)'][7:10])
    fitLines = [[slopeAfter15000,interceptAfter15000,slopeBefore15000,interceptBefore15000],
                [slopeAfter25000,interceptAfter25000,slopeBefore25000,interceptBefore25000],
                [slopeAfter35000,interceptAfter35000,slopeBefore35000,interceptBefore35000,]]
    return fitLines

roundElbowFits = trendline(roundElbow)
cappedTeeFits = trendline(cappedTee)

# Calculate friction factors
roundFrictionFactors = []
i=0
for lines in roundElbowFits:
    roundFrictionFactors = np.concatenate([roundFrictionFactors,[(lines[0] + lines[2])/(density*velocities[i]**2)]])
    i += 1

cappedFrictionFactors = []
i = 0
for lines in cappedTeeFits:
    cappedFrictionFactors = np.concatenate([cappedFrictionFactors,[(lines[0] + lines[2])/(density*velocities[i]**2)]])
    i += 1


# Calculate surface roughness

# Calculate Pressure drops
i = 0
roundPressureDrops = []
for lines in roundElbowFits:
    roundPressureDrops = np.concatenate([roundPressureDrops,[lines[1]-lines[3]]])
    i += 1

i = 0
cappedPressureDrops = []
for lines in cappedTeeFits:
    cappedPressureDrops = np.concatenate([cappedPressureDrops,[lines[1]-lines[3]]])
    i += 1

# Calculate minor loss factor
roundMinorFactors = []
i = 0
for lines in roundElbowFits:
    roundMinorFactors = np.concatenate([roundMinorFactors,[2*roundPressureDrops[i]/(density*velocities[i]**2)]])
    i += 1
avgRoundMinorFactor = sum(roundMinorFactors)/3

cappedMinorFactors = []
i = 0
for lines in cappedTeeFits:
    cappedMinorFactors = np.concatenate([cappedMinorFactors,[2*cappedPressureDrops[i]/(density*velocities[i]**2)]])
    i += 1
avgCappedMinorFactor = sum(cappedMinorFactors)/3

# Plotting
sns.set_theme()

plt.figure(1)
plt.title('Round Elbow Pressure Change vs Position')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 15000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 25000)')
sns.scatterplot(data=roundElbow,x='Position [m]',y='Pressure Drop [Pa] (R_e = 35000)')
for lines in roundElbowFits:
    pressureDrops = lines[0]*roundElbow['Position [m]'] + lines[1]
    plt.plot(roundElbow['Position [m]'],pressureDrops)
plt.legend(labels=['R_e=15000','R_e=25000','R_e=35000','LoB (R_e=15000)','LoB (R_e=25000)','LoB (R_e=35000)'],loc='lower right')
plt.ylabel('Pressure Change [Pa]')

plt.figure(2)
plt.title('Capped Tee Pressure Change vs Position')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 15000)')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 25000)')
sns.scatterplot(data=cappedTee,x='Position [m]',y='Pressure Drop [Pa] (R_e = 35000)')
for lines in cappedTeeFits:
    pressureDrops = lines[0]*cappedTee['Position [m]'] + lines[1]
    plt.plot(cappedTee['Position [m]'],pressureDrops)
plt.legend(labels=['R_e=15000','R_e=25000','R_e=35000','LoB (R_e=15000)','LoB (R_e=25000)','LoB (R_e=35000)'],loc='lower right')
plt.ylabel('Pressure Change [Pa]')

# plt.show()