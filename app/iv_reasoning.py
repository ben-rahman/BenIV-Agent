# iv_reasoning.py

import pandas as pd
import numpy as np
from dowhy import CausalModel

# Simulasi data sintetis
np.random.seed(0)
N = 1000
Z = np.random.binomial(1, 0.5, N)  # Instrument
X = Z + np.random.normal(0, 0.1, N)  # Treatment
Y = 2 * X + np.random.normal(0, 0.1, N)  # Outcome

data = pd.DataFrame({"Z": Z, "X": X, "Y": Y})

# Bangun model kausal
model = CausalModel(
    data=data,
    treatment="X",
    outcome="Y",
    instruments=["Z"]
)

identified_estimand = model.identify_effect()
estimate = model.estimate_effect(identified_estimand,
                                 method_name="iv.instrumental_variable")

print("Estimated causal effect (IV):", estimate.value)
