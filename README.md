# QUCT: The Universal Criticality Parameter (γ*) and the Origin of GUE Statistics in Riemann Zeros

## 💡 Status: Final Monograph Draft (v3.0) 

**Author:** Igor Chechelnitsky
**Date:** 20 November 2025
**zenodo.org** https://zenodo.org/records/17661602
---

### **ABSTRACT**
This repository contains the **Qadmon Universal Criticality Theory (QUCT)**, an analytical framework that derives the spectral parameters of the Riemann zeta zeros from first principles. We model spectral coherence via an Integral Variational Functional $F(\gamma)$, where the unique critical point $\gamma^*$ is defined by the condition $F'''(\gamma^*) = 0$. For the GUE ($\beta=2$) class, QUCT predicts the critical constant: $\mathbf{\gamma^* \approx 0.3958242245}$. This value is rigorously validated against $10^6$ nontrivial Riemann zeros.

---

### **1. CORE ANALYTICAL RESULT (Theorem 1)**
The critical parameter $\gamma^*$ is derived from the Master Analytical Equation, $2\mu = a^3 A e^{-a\gamma^*} + b^3 B e^{-b\gamma^*}$, yielding:

$$\boxed{\gamma^* \approx 0.3958242245}$$

### **2. REPRODUCIBILITY (Python Scripts)**
The results are fully reproducible. All code is located in the **`/code`** directory.

### **3. INSTALLATION AND USAGE**

1.  **Dependencies:** Ensure Python is installed.
    ```bash
    pip install -r requirements.txt
    ```
2.  **Verify Functional Root (Run from the root directory):**
    ```bash
    python code/quct_functional.py
    ```
3.  **Run Riemann Test (Run from the root directory):**
    ```bash
    python code/quct_riemann_test.py
    ```

### **4. FULL MONOGRAPH TEXT**
The complete mathematical proofs, formal derivations, and theoretical context are provided in the LaTeX documents located in the **`/docs`** directory.
