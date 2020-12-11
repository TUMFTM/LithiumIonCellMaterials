
from cells import samsung_48G, samsung_25R, LG_HB4, A123, LG_HB2, LG_HG2, samsung_30Q, sony_VTC5A, sony_VTC6
from geometric import geometric_calculation_cylindric
from calculate_masses_ah_g import calculate_masses_ah_g
from calculate_masses_density_based import calculate_masses_density_based
from calculate_masses_inactive import calculate_masses_inactive, calculate_total_mass
from calculate_masses_top_down import calculate_masses_top_down


'''
Settings
--------
Choose by assigning one if the following to the variable cell:
samsung_48G, samsung_25R, LG_HB4, A123, LG_HB2, LG_HG2, samsung_30Q, sony_VTC5A, sony_VTC6
'''

cell=A123
# cell = samsung_48G
# cell = samsung_25R
# cell = LG_HB4
# cell = LG_HG2
# cell=sony_VTC6

gc = geometric_calculation_cylindric(cell)
print("--------------------------------------------")

inactive_masses = calculate_masses_inactive(cell, gc)
print("--------------------------------------------")


masses_ahg = calculate_masses_ah_g(cell, gc)
calculate_total_mass(inactive_masses, masses_ahg, cell, gc)
print("--------------------------------------------")

masses_density = calculate_masses_density_based(cell, gc)
calculate_total_mass(inactive_masses, masses_density, cell, gc)
print("--------------------------------------------")

calculate_masses_top_down(cell)
print("--------------------------------------------")
