# CSPC - Computer Science for Physics and Chemistry
My coursework repository.Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
4Computer Science for Physics and Chemistry
PW1 – Lab A
**What I built:**
- Set up the CSPC repository and created the Conda environment with python, NumPy, and pytest
- added the decay simulation, wrote additional tests, compared the speed of the python loop with the numpy implementation.
**Speed comparison (loop vs NumPy):**
- loop : 1.5911s
- numpy : 0.0002s
- speed-up: 9002.83 x faster
**Tests:** all passing?
yes, 3 passed
**Conclusion:**
- In this lab, I learned how Git and Github can help me organize my coursework and track changes with commits and branches. I also used pytest and Python loop with NumPy, which showed me why optimized functions are useful for larger simulations.                      


## PW1 Lab B
- Checked out the radioactive decay data (`decay_observed.csv`) and plotted it side-by-side with the analytical exponential decay curve ($N_0 e^{-\lambda t}$) to see how well they match[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span).
- Set up a simple `Snakefile` so that running `snakemake` automatically builds and updates `figure.png`[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

## PW2 Lab A
- Loaded the free-fall tracking data (`freefall.csv`) and calculated velocity and acceleration using numerical differentiation. 
- Got a mean acceleration of around -8.58 m/s², and noticed how taking the derivative twice makes the data look super noisy because of tiny measurement errors.
- Integrated the acceleration back up to successfully recover the original position and velocity profiles.

