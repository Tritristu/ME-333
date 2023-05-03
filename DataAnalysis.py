import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
atmPressure = 1.0108*101325 # Pa
temp = 273.15 + (5/9)*(72.1 - 32) # Kelvin
airGasConst = 287 # kJ/kg*K
middle = 25 # mm
inputPressure = 30 # mmHg
volumeFlowRate = inputPressure*2.5422e-4 #m**3/s
scaleMass = 2.2 #g

# Reading in data
data = pd.read_csv('Lab 1 data.csv')

# Positional data
distance = data['Distance [mm]'] # mm
position = np.abs(distance - 25)*1e-3 # m

# Calculate Quantities
guagePressure = (data['Trial 1'] + data['Trial 2'] + data['Trial 3'])*133.322/3 # Pa
absPressure = atmPressure + guagePressure
density = absPressure/(temp*airGasConst)
velocity = np.sqrt(2*guagePressure/density)
scaleForce = scaleMass*9.81e-3

# Estimating flow rates with velocity
estVolFlowRate = np.trapz((np.pi*position)*velocity,x=distance*1e-3)
massFlowRate = np.trapz(density*(np.pi*position)*velocity,x=distance*1e-3)
forceExerted = np.trapz(density*(np.pi*position)*velocity**2,x=distance*1e-3)

# Error Calculations
fluxError = np.abs(volumeFlowRate-estVolFlowRate)/volumeFlowRate
forceError = np.abs(scaleForce-forceExerted)/scaleForce

print('Incline Manometer estimated vol flow rate (m^3/s):',volumeFlowRate)
print('Velocity estimated vol flow rate (m^3/s):',estVolFlowRate)
print('Mass flux (kg/s):',massFlowRate)
print('Actual Force (N):',scaleForce)
print('Calculated Force (N):',forceExerted)
print('Volumetric Flux Error:', fluxError)
print('Force Balance Error:', forceError)

# Effects of changing jet height
jetPos = data['Jet Position'] # cm
forceBalance = (data['Balance 1'] + data['Balance 2'] + data['Balance 3'])*9.81e-3/3 # N


# Velocity Profile
fig = plt.figure(1)
ax = fig.gca()
ax.plot(distance,velocity)
ax.set_xlim(left = 0,right=50)
ax.set_ylim(bottom = 0,top=3.5)
plt.title("Velocity vs Distance from Jet Wall")
plt.ylabel('Velocity (m/s)')
plt.xlabel('Distance from the Jet Wall (mm)')
# plt.legend()

# Apparent force with respect to distance from jet
fig = plt.figure(2)
ax = fig.gca()
ax.plot(jetPos,forceBalance)
ax.set_xlim(left = 0,right=13)
ax.set_ylim(bottom = -0.06,top=0.03)
plt.title("Force vs distance from the Jet")
plt.ylabel('Force (N)')
plt.xlabel('Distance from the Jet (cm)')
# plt.legend()
plt.show()

