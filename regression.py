from os import X_OK
import numpy as np
import statsmodels.api as sm
import pandas as pd

independent_variable = df.drop(columns=['note/journal','category'])
dependent_variable = df['note/journal']


# Create a matrix of independent variables
X = independent_variable

# Add a constant column to the matrix
X = sm.add_constant(X)

# Create the ordinary least squares (OLS) model (dependent, independent)
model = sm.OLS(dependent_variable, X)

# Fit the model to the data
results = model.fit()

# Show Summary
print(results.summary())
