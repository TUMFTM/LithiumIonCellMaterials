from cells import PHEV2, pouch_fantasy1, pouch_fantasy2, BEV2, EIG_ePLB_C020, Schmalstieg_pris, Kokam_7_5AH, eGolf_UF261591
from geometric import geometric_calculation_prismatic
from calculate_masses_ah_g import calculate_masses_ah_g
from calculate_masses_density_based import calculate_masses_density_based
from calculate_masses_inactive import calculate_masses_inactive, calculate_total_mass
from calculate_masses_top_down import calculate_masses_top_down
from util import theoretical_capacity


'''
Settings
--------
Choose by assigning one if the following to the variable cell:
PHEV2, pouch_fantasy1, pouch_fantasy2, BEV2, EIG_ePLB_C020, Schmalstieg_pris, Kokam_7_5AH, eGolf_UF261591
'''

# cell=PHEV2
cell=EIG_ePLB_C020
# cell=Schmalstieg_pris
# cell=Kokam_7_5AH
cell=eGolf_UF261591

gc = geometric_calculation_prismatic(cell)
print("--------------------------------------------")

inactive_masses = calculate_masses_inactive(cell, gc)
print("--------------------------------------------")

mass_ahg = calculate_masses_ah_g(cell, gc)
total_mass_ah_g = calculate_total_mass(inactive_masses, mass_ahg, cell, gc)
print("--------------------------------------------")

masses_density = calculate_masses_density_based(cell, gc)
total_mass_density = calculate_total_mass(inactive_masses, masses_density, cell, gc)
print("--------------------------------------------")

# mean value weight:
total_mass = (total_mass_density["total_mass"] + total_mass_ah_g["total_mass"])/2
mass_topdown = calculate_masses_top_down(cell, total_mass=total_mass)

c_theo = theoretical_capacity(cell, gc)
print(0)