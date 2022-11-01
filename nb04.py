import pandas as pd

df = pd.read_csv('agilytic/dataset1.csv', sep=';')

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
