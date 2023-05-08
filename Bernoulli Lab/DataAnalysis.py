import pandas as pd
import numpy as np
import seaborn as sns

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
avgTime2 = (116+116)/3
avgTime3 = (19.17+18.63+19.09)/3

volFlux1 = 6e-3/avgTime1
volFlux2 = 6e-3/avgTime2
volFlux3 = 2e-3/avgTime3

print('Trial 1 Volumetric Flux:',avgTime1)
print('Trial 2 Volumetric Flux:',avgTime2)
print('Trial 3 Average Volumetric Flux:',avgTime3)

# Bernoulli Velocity



# Mass Conservation velocity
massFLux1 = density*volFlux1
massFLux2 = density*volFlux2
massFLux3 = density*volFlux3

trialOne['Mass Conservation Velocity (m/s)'] = massFLux1/(density*trialOne['Area (m^2)'])
trialTwo['Mass Conservation Velocity (m/s)'] = massFLux2/(density*trialTwo['Area (m^2)'])
trialThree['Mass Conservation Velocity (m/s)'] = massFLux3/(density*trialThree['Area (m^2)'])

# Plotting

# sns.lineplot(data=trialOne,x='Duct Distance(mm)',y='Static Head (mm)')




