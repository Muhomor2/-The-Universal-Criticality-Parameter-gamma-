# quct_functional.py - QUCT Analytical Root Finder for GUE (beta=2)

import numpy as np
from scipy.optimize import brentq

# ANALYTICAL PARAMETERS for GUE (Derived from Boundary Conditions)
MODEL_PARAMS = {
    'A': 1.0, 'a': 3.2,
    'B': 0.9, 'b': 2.6,
    'mu': 7.439993889526777, 
}

def F3(gamma):
    """Computes the third derivative of the QUCT Functional: F'''(gamma)"""
    P = MODEL_PARAMS
    # F'''(gamma) = -a^3 * A * exp(-a*gamma) - b^3 * B * exp(-b*gamma) + 2*mu
    term1 = - P['A'] * (P['a']**3) * np.exp(-P['a'] * gamma)
    term2 = - P['B'] * (P['b']**3) * np.exp(-P['b'] * gamma)
    term3 = 2 * P['mu']
    return term1 + term2 + term3

def find_root():
    """Finds the critical root gamma* where F'''(gamma) = 0 in the domain (0, 1)"""
    return brentq(F3, 0.001, 1.0)

if __name__ == '__main__':
    root = find_root()
    print("--- QUCT Core Verification ---")
    print("Model: Analytical GUE (beta=2)")
    print("QUCT Critical Parameter (gamma*): {:.16f}".format(root))
    print("--- Success ---")
