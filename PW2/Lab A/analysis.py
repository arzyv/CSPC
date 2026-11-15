"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v and acceleration a
v = np.gradient(y, t)
a = np.gradient(v, t)
print("mean a:", np.mean(a))

# TODO 3: integrate a back up to recover velocity and position
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
ax1.plot(t, y, label="Original Position", color="blue")
ax1.plot(t, y_recovered, label="Recovered Position", color="orange", linestyle="--")
ax1.set_ylabel("Position (m)")
ax1.legend()
ax1.grid(True)

# Panel 2: Velocity
ax2.plot(t, v, label="Velocity", color="green")
ax2.set_ylabel("Velocity (m/s)")
ax2.legend()
ax2.grid(True)

# Panel 3: Acceleration
ax3.plot(t, a, label="Noisy Acceleration", color="red", alpha=0.5)
ax3.axhline(-9.81, color="black", linestyle="--", label="True g (-9.81)")
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.set_xlabel("Time (s)")
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("Saved plot as motion.png successfully!")
