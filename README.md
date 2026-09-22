# CSPC - Computer Science for Physics and Chemistry
My coursework repository.Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations

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
**Reproducibility test**
- My partner cloned my repository and run the tests on their laptop
- all 3 tests passed
- No changes were needed
