'''
examples from:
https://www.youtube.com/watch?v=8Aw45HN5lnA&ab_channel=TheOrganicChemistryTutor

null hypothesis H0: population from city is tall 168
alternative hypothesis H1: population is tall not 168

# ## Z vs T values

# HOW MNAY STDEV FROM THE MEAN MY RESULT IS?

z_score = (xbar - mu) / sigma
normal distribution, population standard deviation sigma is known, and n>30.

t_score (aka Student's T-Distribution) = (xbar - mu) / (s/sqrt(n))
normal distribution, population standard deviation (sigma) is NOT known,
but the sample standard deviation (s) is known, and n<30.

Summary: If n > 30, z ~ t.
If the population standard deviation s is available and n > 30,
t_score can be used with sigma instead of the s.
'''
#number of observation
n = 36

#mean
X_pop = 169.5
X_obs = 168

#sample stdev
s = 3.9
# %% codecell
#confidence value
c = 0.95
#significance value
a = 1 - c
# %% codecell
import numpy as np
from scipy import stats
import math

# alpha to critical
alpha = 0.05
AL = 1-alpha/n_sided
n_sided = 2 # 2-sided test
z_crit = stats.norm.ppf(AL)
print(z_crit) # 1.959963984540054

z_value = ( X_pop - X_obs ) / (s / math.sqrt(n))

print(z_value)
# critical to alpha
alpha_z = stats.norm.sf(z_value) * n_sided
print(alpha_z) # 0.05
# %% codecell
#t_crit = stats.t.ppf(alpha/n_sided, n)
#print(t_crit)
#alpha_t = stats.norm.sf(t_crit) * n_sided
#print(alpha_t) # 0.05
# %% markdown
# ## Example 1
# %% codecell
'''
H0: engine will not break before 5yrs
HA: engine will break before 5 yrs
'''
n = 36
X_pop = 168
X_obs = 169.5
s = 3.9

alpha = 0.05
AL = 1-alpha/n_sided
n_sided = 2
z_crit = stats.norm.ppf(AL)

z_value = ( X_obs - X_pop ) / (s / math.sqrt(n))
p_value = stats.norm.sf(z_value) * n_sided

print('critical z   =', z_crit)
print('calculated z =', z_value)
print('p value      =', p_value)

if p_value <= alpha:
    print('Reject null hypothesis (p<=a)')
else:
    print('Fail to reject null hypothesis (p>a)')
# %% markdown
# ## Example 2
# %% codecell
'''
H0: engine will not break before 5yrs
HA: engine will break before 5 yrs
'''
n = 40
X_pop = 5
X_obs = 4.8
s = 0.50

  = 0.02
AL = 1-alpha/n_sided
n_sided = 1
z_crit = stats.norm.ppf(AL)

z_value = ( X_obs - X_pop ) / (s / math.sqrt(n))
p_value = min( 1 - stats.norm.sf(z_value) * n_sided, stats.norm.sf(z_value) * n_sided )

print('critical z   =', z_crit)
print('calculated z =', z_value)
print('p value      =', p_value)

if p_value <= alpha:
    print('Reject null hypothesis (p<=a)')
else:
    print('Fail to reject null hypothesis (p>a)')
# %% markdown
# ## Example 3
# %% codecell
#from https://www.youtube.com/watch?v=eyknGvncKLw&t=43s&ab_channel=DrNic%27sMathsandStats
'''
H0: 70gr of peanuts per 200 gr of chocolate
HA: < 70gr of peanuts per 200 gr of chocolate
'''
n = 30
X_pop = 70
X_obs = 68.7
s = 5

alpha = 0.02 #significance, confidance c = 1 - alpha
AL = 1-alpha/n_sided
n_sided = 2
z_crit = stats.norm.ppf(AL)

z_value = ( X_obs - X_pop ) / (s / math.sqrt(n))
p_value = stats.norm.sf(z_value) * n_sided

print('critical z   =', z_crit)
print('calculated z =', z_value)
print('p value      =', p_value)

if p_value <= alpha:
    print('Reject null hypothesis (p<=a)')
else:
    print('Fail to reject null hypothesis (p>a)')
# %% markdown
# # Example 4
# %% codecell
import pandas as pd

df = pd.read_csv('agilytic/dataset1.csv', sep=';')
# %% codecell
df.columns
# %% codecell
male_high_df = df.loc[ df['sex'] == 'Male' ].loc[
    df['taxable income amount'] == 1 ]
male_low_df = df.loc[ df['sex'] == 'Male' ].loc[
    df['taxable income amount'] == 0 ]
female_high_df = df.loc[ df['sex'] == 'Female' ].loc[
    df['taxable income amount'] == 1 ]
female_low_df = df.loc[ df['sex'] == 'Female' ].loc[
    df['taxable income amount'] == 0 ]
# %% codecell
male_df = df.loc[ df['sex'] == 'Male' ]
female_df = df.loc[ df['sex'] == 'Female' ]

high_df = df.loc[ df['taxable income amount'] == 1 ]
low_df = df.loc[ df['taxable income amount'] == 0 ]
# %% codecell
print(len(male_high_df))
print(len(male_low_df))
print(len(female_high_df))
print(len(female_low_df))
# %% codecell
'''
H0: man report the same as woman
H2: man do not report the same as woman
'''
def variance_bool(p,n):
    return p*(1-p)/n

high_ratio_male = len(male_high_df) / len(male_df)
std_HRM = math.sqrt(variance_bool(high_ratio_male, len(male_df)))
high_ratio_female = len(female_high_df) / len(female_df)
std_HRF = math.sqrt(variance_bool(high_ratio_female, len(female_df)))

print(high_ratio_male, std_HRM)
print(high_ratio_female, std_HRF)

# %% codecell
from scipy.stats import binom_test
print(len(male_high_df), len(high_df), len(male_high_df)/len(high_df) )
print(len(female_high_df), len(high_df), len(female_high_df)/len(high_df))

print(binom_test(len(male_high_df), len(high_df))) #, 0.5, alternative="two-sided"))
print(binom_test(len(female_high_df), len(high_df)))#, 0.5, alternative="two-sided"))

print(len(male_low_df), len(low_df), len(male_low_df)/len(low_df) )
print(len(female_low_df), len(low_df), len(female_low_df)/len(low_df))

print(binom_test(len(male_low_df), len(low_df), 0.5, alternative="two-sided"))
print(binom_test(len(female_low_df), len(low_df), 0.5, alternative="two-sided"))
# %% codecell
binom_test(32, 46, 0.5, alternative="two-sided")
# %% codecell
