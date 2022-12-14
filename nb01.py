from scipy import stats
import math
'''
H0: population is 169.5 cm tall on average
H1: population is 168 cm tall on average
'''
#number of observations
n = 36

#mean
X_pop = 169.5
X_obs = 168

#sample stdev
s = 3.9
#confidence value
c = 0.95
#significance value
alpha = 1 - c

n_sided = 2 # 2-sided test
AL = 1-alpha/n_sided
z_crit = stats.norm.ppf(AL)
print(z_crit) # 1.959963984540054

z_value = ( X_pop - X_obs ) / (s / math.sqrt(n))
# critical to alpha
p_value = stats.norm.sf(z_value) * n_sided

print('critical z   =', z_crit)
print('calculated z =', z_value)
print('p value      =', p_value)

if p_value <= alpha:
    print('Reject null hypothesis (p<=a)')
else:
    print('Fail to reject null hypothesis (p>a)')
