'''
H0: engine will not break before 5yrs
HA: engine will break before 5 yrs
'''
n = 36
X_pop = 168
X_obs = 169.5
s = 3.9

alpha = 0.05
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
