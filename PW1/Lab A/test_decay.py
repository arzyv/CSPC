"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_mean_matches_analytical():
    NO = 1000
    lam = 0.4
    dt = 0.05
    steps = 100
    results = [simulate(NO, lam, dt=dt, steps=steps, seed=seed)[-1] for seed  in range(100)]
    mean = np.mean(results)
    expected = NO * np.exp(-lam * dt* steps)
    assert mean == pytest.approx(expected, rel=0.05)
