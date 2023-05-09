import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Reading in data
trialOne = pd.read_csv('Bernoulli Lab\Trial1.csv')
trialTwo = pd.read_csv('Bernoulli Lab\Trial2.csv')
trialThree = pd.read_csv('Bernoulli Lab\Trial3.csv')

# Useful Constants
density = 998.23 # units kg/m**3 at 20C
gravity = 9.81 # units m/s**2

# Area Calculations
trialOne['Area (m^2)'] = (np.pi/4)*(trialOne['Duct Diameter (mm)']*1e-3)**2
trialTwo['Area (m^2)'] = (np.pi/4)*(trialTwo['Duct Diameter (mm)']*1e-3)**2
trialThree['Area (m^2)'] = (np.pi/4)*(trialThree['Duct Diameter (mm)']*1e-3)**2

# Volume Flow rate Calculations
avgTime1 = (53+60+59)/3
avgTime2 = (116+128+116)/3
avgTime3 = (19.17+18.63+19.09)/3

volFlux1 = 6e-3/avgTime1
volFlux2 = 6e-3/avgTime2
volFlux3 = 2e-3/avgTime3

print('Trial 1 Volumetric Flux:',avgTime1)
print('Trial 2 Volumetric Flux:',avgTime2)
print('Trial 3 Average Volumetric Flux:',avgTime3)

# Bernoulli Velocity
trialOne['Bernoulli Velocity (m/s)'] = np.sqrt(2e-3*gravity*(trialOne['Static Head (mm)'][0] - trialOne['Static Head (mm)']))
trialTwo['Bernoulli Velocity (m/s)'] = np.sqrt(2e-3*gravity*(trialTwo['Static Head (mm)'][0] - trialTwo['Static Head (mm)']))
trialThree['Bernoulli Max Velocity (m/s)'] = np.sqrt(2e-3*gravity*(trialThree['Static Head Max (mm)'][0] - trialThree['Static Head Max (mm)']))
# trialThree['Bernoulli Min Velocity (m/s)'] = np.sqrt(2e-3*gravity*(trialThree['Static Head Max (mm)'][0] - trialThree['Static Head Min (mm)']))
trialThree['Bernoulli Min Velocity (m/s)'] = np.sqrt(2e-3*gravity*(trialThree['Static Head Min (mm)'][0] - trialThree['Static Head Min (mm)']))


# Mass Conservation velocity
massFLux1 = density*volFlux1
massFLux2 = density*volFlux2
massFLux3 = density*volFlux3

trialOne['Mass Conservation Velocity (m/s)'] = massFLux1/(density*trialOne['Area (m^2)'])
trialTwo['Mass Conservation Velocity (m/s)'] = massFLux2/(density*trialTwo['Area (m^2)'])
trialThree['Mass Conservation Velocity (m/s)'] = massFLux3/(density*trialThree['Area (m^2)'])

# Plotting
sns.set_theme()

# Trial 1
plt.figure(1)
plt.title('Trial 1 Static Head vs Duct Distance')
sns.lineplot(data=trialOne,x='Duct Distance (mm)',y='Static Head (mm)')
plt.xlim(0,145)
plt.ylim(0,250)

plt.figure(2)
plt.title('Trial 1 Velocity vs Duct Distance')
sns.lineplot(data=trialOne,x='Duct Distance (mm)',y='Bernoulli Velocity (m/s)')
sns.lineplot(data=trialOne,x='Duct Distance (mm)',y='Mass Conservation Velocity (m/s)',color='orange')
plt.xlim(0,145)
plt.legend(labels=['Bernoulli','Mass Conservation'])
plt.ylabel('Velocity (m/s)')
plt.ylim(0,2)

# Trial 2
plt.figure(3)
plt.title('Trial 1 Static Head vs Duct Distance')
sns.lineplot(data=trialTwo,x='Duct Distance (mm)',y='Static Head (mm)')
plt.xlim(0,145)
plt.ylim(0,200)

plt.figure(4)
plt.title('Trial 2 Velocity vs Duct Distance')
sns.lineplot(data=trialTwo,x='Duct Distance (mm)',y='Bernoulli Velocity (m/s)')
sns.lineplot(data=trialTwo,x='Duct Distance (mm)',y='Mass Conservation Velocity (m/s)',color='orange')
plt.legend(labels=['Bernoulli','Mass Conservation'])
plt.ylabel('Velocity (m/s)')
plt.xlim(0,145)
plt.ylim(0,1)

# Trial 3
plt.figure(5)
plt.fill_between(x=trialThree['Duct Distance (mm)'], y1=trialThree['Static Head Max (mm)'], y2=trialThree['Static Head Min (mm)'], alpha=0.3, label='Pressure Range')
plt.xlim(0,145)
plt.ylim(0,250)
plt.title("Trial 3 Static Head vs Duct Distance")
plt.ylabel('Static Head Max (mm)')
plt.xlabel('Duct Distance (mm)')
plt.legend()

plt.figure(6)
plt.fill_between(x=trialThree['Duct Distance (mm)'], y1=trialThree['Bernoulli Max Velocity (m/s)'], y2=trialThree['Bernoulli Min Velocity (m/s)'], alpha=0.7)
sns.lineplot(data=trialThree,x='Duct Distance (mm)',y='Mass Conservation Velocity (m/s)',color='orange')
plt.plot(trialThree['Duct Distance (mm)'],trialThree['Bernoulli Max Velocity (m/s)'],color='blue')
plt.plot(trialThree['Duct Distance (mm)'],trialThree['Bernoulli Min Velocity (m/s)'],color='blue')
plt.xlim(0,145)
plt.ylim(0,1.75)
plt.title("Trial 3 Velocity vs Duct Distance")
plt.ylabel('Velocity (m/s)')
plt.legend(labels=['Bernoulli','Mass Conservation'])


plt.show()




