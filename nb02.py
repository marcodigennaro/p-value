from scipy import stats
import math
'''
H0: engine will not break before 5yrs
HA: engine will break before 5 yrs
'''
#number of observations
n = 40

#mean
X_pop = 5
X_obs = 4.8

#sample stdev
s = 0.50
#confidence value
c = 0.98
#significance value
alpha = 1 - c

n_sided = 1
AL = 1-alpha/n_sided
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
