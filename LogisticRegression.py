import numpy as np
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('regression.csv')
independent_variable = df.drop(columns=['note/journal','category'])
dependent_variable = df['note/journal']


# Create a matrix of independent variables
X = independent_variable

# Add a constant column to the matrix
X = sm.add_constant(X)

# Create the logistic regression model (dependent, independent)
model = sm.Logit(dependent_variable, X)

# Fit the model to the data
results = model.fit()

# Print the summary of results
print(results.summary())

# Get the coefficient estimates
coefficients = results.params

# Get the odds ratios by exponentiating the coefficients
odds_ratios = np.exp(coefficients)

# Print the odds ratios
print("Odds Ratios:")
for i, var in enumerate(['const', 'independent_variable', 'dependent_variable']):
    print(f"{var}: {odds_ratios[i]}")
