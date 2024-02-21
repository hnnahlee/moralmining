from typing_extensions import TypeAlias
import scipy.stats as stats

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(x,y)

# Print the results
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

# Perform independent samples t-test
t_statistic, p_value = stats.ttest_ind(x,y)

# Print the results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
