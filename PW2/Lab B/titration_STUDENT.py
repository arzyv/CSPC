"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
ph = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(ph, V)
idx = np.argmax(slope)
eq_vol = V[idx]
print("equivalence point volume:", eq_vol)

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)

ax1.plot(V, ph)
ax1.axvline(eq_vol, color='red', linestyle='--')
ax1.set_title("pH Curve")
ax1.set_xlabel("Volume")
ax1.set_ylabel("pH")

ax2.plot(V, slope)
ax2.axvline(eq_vol, color='red', linestyle='--')
ax2.set_title("slope (dpH/dV)")
ax2.set_xlabel("volume")
ax2.set_ylabel("skope")

plt.savefig("titration.png", dpi=300)
