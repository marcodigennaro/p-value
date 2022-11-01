from scipy import stats
import math
'''
H0: 70gr of peanuts per 200 gr of chocolate
HA: < 70gr of peanuts per 200 gr of chocolate
'''
#number of observations
n = 30

#mean
X_pop = 70
X_obs = 68.7

#sample STDEV
s = 5
alpha = 0.02 #significance, confidance c = 1 - alpha

n_sided = 2
AL = 1-alpha/n_sided
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
