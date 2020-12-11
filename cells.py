'''
This file contains the cells.
Each cell has static information in a dictionary
'''


############## Rundzellen ############################################
# Alle aus Lain2019
housing_thickness = 0.2
samsung_25R = {
    "name":"Samsung_25R",
    "type": "18650",
    "design": "capacity",
    "cat-chem":"NCA+NMC622",
    "an-chem":"graphite-si",
    "capacity": 2.57, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.2,  # unklar
    "specific_capacity_paper": 0.179,  # Ah/g
    "ease_packaging_factor": 1.05,
    "D0":  4 * 10**-3,
    "D1": 18 * 10**-3,
    "l":  65 * 10**-3,
    "l_jellyroll": (60-housing_thickness)* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.09,
    "an_porosity": 0.2,
    "cu" : 10 * 10**-6,
    "an" : 43 * 10**-6,
    "sep" :10 * 10**-6,
    "cat": 38 * 10**-6,
    "al" : 14 * 10**-6,
    "sep2" :10 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 43.8
}

samsung_48G = {
    "name":"Samsung_48G",
    "type": "21700",
    "design": "capacity",
    "cat-chem":"NCA",
    "an-chem":"graphite-si",
    "capacity": 4.838, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.1,  # unklar
    # "specific_capacity_paper": 0.199,  # Ah/g
    "ease_packaging_factor": 1,
    "D0": 4 * 10**-3,
    "D1": 21 * 10**-3,
    "l":  70 * 10**-3,
    "l_jellyroll": (65-(housing_thickness))* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95, # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.13,
    "an_porosity": 0.22,
    "cu" : 10 * 10**-6,
    "an" : 85 * 10**-6,
    "sep" : 8 * 10**-6,
    "cat": 71 * 10**-6,
    "al" : 12 * 10**-6,
    "sep2" :8 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 67.4
}

samsung_30Q = {
    "name":"samsung_30Q",
    "type": "18650",
    "design": "capacity",
    "cat-chem":"NCA",
    "an-chem":"graphite-si",
    "capacity": 3, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.1,  # unklar
    # "specific_capacity_paper": 0.199,  # Ah/g
    "ease_packaging_factor": 1.1,
    "D0":  4 * 10**-3,
    "D1": 18 * 10**-3,
    "l":  65 * 10**-3,
    "l_jellyroll": (65-(housing_thickness))* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95, # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.09,
    "an_porosity": 0.25,
    "cu" : 10 * 10**-6,
    "an" : 45 * 10**-6,
    "sep" : 8 * 10**-6,
    "cat": 44 * 10**-6,
    "al" : 14 * 10**-6,
    "sep2" :8 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 45.8
}

sony_VTC5A = {
    "name":"sony_VTC5A",
    "type": "18650",
    "design":"power",
    "cat-chem":"NCA",
    "an-chem":"graphite-si",
    "capacity": 2.5, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.1,  # unklar
    # "specific_capacity_paper": 0.199,  # Ah/g
    "ease_packaging_factor": 1.1,
    "D0":  4 * 10**-3,
    "D1": 18 * 10**-3,
    "l":  65 * 10**-3,
    "l_jellyroll": (65-(housing_thickness))* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95, # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.13,
    "an_porosity": 0.27,
    "cu" : 14 * 10**-6,
    "an" : 47 * 10**-6,
    "sep" : 8 * 10**-6,
    "cat": 43 * 10**-6,
    "al" : 15 * 10**-6,
    "sep2" :8 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 47.9
}

sony_VTC6 = {
    "name":"sony_VTC6",
    "type": "18650",
    "design": "capacity",
    "cat-chem":"NCA",
    "an-chem":"graphite-si",
    "capacity": 3, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.1,  # unklar
    # "specific_capacity_paper": 0.199,  # Ah/g
    "ease_packaging_factor": 1.1,
    "D0":  4 * 10**-3,
    "D1": 18 * 10**-3,
    "l":  65 * 10**-3,
    "l_jellyroll": (65-(housing_thickness))* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95, # g/cm³
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.15,
    "an_porosity": 0.38,
    "cu" : 10 * 10**-6,
    "an" : 53 * 10**-6,
    "sep" : 7 * 10**-6,
    "cat": 52 * 10**-6,
    "al" : 12 * 10**-6,
    "sep2" :7 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 46.9
}

A123={
    "name":"A123",
    "type": "18650",
    "design":"power",
    "cat-chem": "LFP",
    "an-chem": "graphite",
    "capacity": 1.1,  # Ah
    "anode_overhang": 1.1,
    "specific_capacity_paper": 0.116, # aus paper: 0.116,
    "factor_more_capacity_cathode": 1.7,  # unklar
    "ease_packaging_factor": 1.02,
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.79,
    #     "binder": 0.11,
    #     "carbon": 0.10
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.26,
    "an_porosity": 0.25,
    "cu": 10 * 10 ** -6,
    "an": 36 * 10 ** -6,
    "sep": 18 * 10 ** -6,
    "cat": 81 * 10 ** -6,
    "al": 19 * 10 ** -6,
    "sep2": 18 * 10 ** -6,
    "buffer": 0 * 10 ** -6,
    "total_mass": 39.8
}

LG_HB4={
    "name":"LG_HB4",
    "type": "18650",
    "design":"power",
    "cat-chem": "NMC111",
    "an-chem": "graphite",
    "capacity": 1.5,  # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.4,  # unklar
    # "specific_capacity_paper": 0.160, #Ah/g
    "ease_packaging_factor": 1.15, #1.15,
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.26,
    "an_porosity": 0.24,
    "cu": 15 * 10 ** -6,
    "an": 43 * 10 ** -6,
    "sep": 10 * 10 ** -6,
    "cat": 50 * 10 ** -6,
    "al": 25 * 10 ** -6,
    "sep2": 10 * 10 ** -6,
    "buffer": 0 * 10 ** -6,
    "total_mass": 43.1
}

LG_HB2={
    "name":"LG_HB2",
    "type": "18650",
    "design":"power",
    "cat-chem": "NMC532",
    "an-chem": "graphite",
    "capacity": 1.5,  # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.4,  # unklar
    # "specific_capacity_paper": 0.160, #Ah/g
    "ease_packaging_factor": 1.15, #1.15,
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.28,
    "an_porosity": 0.23,
    "cu": 15 * 10 ** -6,
    "an": 44 * 10 ** -6,
    "sep": 10 * 10 ** -6,
    "cat": 43 * 10 ** -6,
    "al": 27 * 10 ** -6,
    "sep2": 10 * 10 ** -6,
    "buffer": 0 * 10 ** -6,
    "total_mass": 43.1
}

LG_HG2={
    "name":"LG_HG2",
    "type": "18650",
    "design": "capacity",
    "cat-chem": "NMC811",
    "an-chem": "graphite-si",
    "capacity": 3,  # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode": 1.05,  # unklar
    # "specific_capacity_paper": 0.160, #Ah/g
    "ease_packaging_factor": 1.04, #1.15,
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.96,
    #     "binder": 0.02,
    #     "carbon": 0.02
    # },
    "cat_activematerial": 0.96,
    "cat_binder": 0.02,
    "cat_conductivecarbon": 0.02,
    "an_activematerial": 0.96,
    "an_binder": 0.02,
    "an_conductivecarbon": 0.02,
    "cat_porosity": 0.17,
    "an_porosity": 0.25,
    "cu": 10 * 10 ** -6,
    "an": 55 * 10 ** -6,
    "sep": 10 * 10 ** -6,
    "cat": 52 * 10 ** -6,
    "al": 10 * 10 ** -6,
    "sep2": 10 * 10 ** -6,
    "buffer": 0 * 10 ** -6,
    "total_mass": 44.8
}
#####################################################################


########### Prismatic cells #########################################
#   _____________
# .-`  -    + .H`|
# |-----B-----|  |
# |           L  |
# |           |  |
# |-----------|.-`
housing_thickness = 0.5
PHEV2 = { # From Liebig2019
    "name":"PHEV2",
    "type": "prismatic",
    "design": "power",
    "structure": "stack",
    "cat-chem":"NMC111",
    "an-chem":"graphite",
    "capacity": 40, # Ah
    "anode_overhang": 1.011,
    "specific_capacity_paper": 0.160,
    "factor_more_capacity_cathode":1.7, # Geschätzt aus Liebig2019
    "h": 0.0265, # abmaße PHEV2 aus Hettesheimer2017 TIEFE
    "l": 0.091, #m BREITE
    "b": 0.148 , #m LÄNGE (2D hoehe)
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.2,
    "an_porosity": 0.3,
    "cu" : 19 * 10**-6,
    "an" : 47.5 * 10**-6,
    "sep" :24.7 * 10**-6,
    "cat": 54.5 * 10**-6,
    "al" : 17.7 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 0
}

BEV2 = {
    "name":"BEV2",
    "type": "prismatic",
    "design": "capacity",
    "structure": "stack",
    "cat-chem":"NMC111",
    "an-chem":"graphite",
    "capacity": 108.9, # Ah
    "anode_overhang": 1.15,
    "factor_more_capacity_cathode":1.16, # Geschätzt aus Liebig2019
    "case_to_stack_layer_factor": 0.8,
    # "case_to_stack_layer_factor": 1,
    "h": 0.045, # abmaße BEV2 aus Hettesheimer2017 TIEFE
    "l": 0.115, #m BREITE
    "b": 0.173 , #m LÄNGE (2D hoehe)
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.2,
    "an_porosity": 0.3,
    "cu" : 15 * 10**-6,
    "an" : 86 * 10**-6,
    "sep" :20 * 10**-6,
    "cat": 78 * 10**-6,
    "al" : 15 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 0
}

Schmalstieg_pris = { # Parameter from Schmalstieg2017
    "name":"Schmalstieg_pris", # PHEV1
    "type": "prismatic",
    "design": "power",
    "structure": "2-wickel",
    "cat-chem":"NMC111",
    "an-chem":"graphite",
    "capacity": 30, # Ah
    "anode_overhang": 1.091, # Aus Schmalstieg berechnet
    "factor_more_capacity_cathode":1.17, # Geschätzt
    # "h": 0.025, # # Übernommen aus cell_geometry_schmalstieg
    # "l": 0.125, #m
    # "b": 0.173 , #m
    # "l_jellyroll": 0.124,
    # "h": 0.0265,  # abmaße PHEV2 aus Hettesheimer2017 TIEFE
    # "l": 0.091,  # m BREITE
    # "b": 0.148,  # m LÄNGE (2D hoehe)
    # "b_jellyroll": 0.124,
    "h": 0.021,  # abmaße PHEV1 aus cellformats_daimler
    "l": 0.085,  # m BREITE
    "b": 0.173,  # m LÄNGE (2D hoehe)
    "b_jellyroll": 0.124,
    "ease_packaging_factor": 1.05,
    "D0": 0 * 10 ** -3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.395,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.88,
    #     "binder": 0.06,
    #     "carbon": 0.06
    # },
    "cat_activematerial": 0.88,
    "cat_binder": 0.06,
    "cat_conductivecarbon": 0.06,
    "an_activematerial": 0.88,
    "an_binder": 0.06,
    "an_conductivecarbon": 0.06,
    "cat_porosity": 0.209,
    "an_porosity": 0.292,
    "cu" : 10 * 10**-6,
    "an" : 46.6 * 10**-6,
    # "an" : 93.2 * 10**-6,
    "sep": 18.7 * 10**-6,
    "cat": 43 * 10**-6,
    # "cat": 86 * 10**-6,
    "al" : 11 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 758.4,
    "cat_total_mass": 136*2,
    "an_total_mass": 115*2,
    "sep_total_mass": 25.7
}

housing_thickness = 0.5
eGolf_UF261591={ # Format vermutlich PHEV2
    "name":"eGolf_UF261591",
    "type": "prismatic",
    "design": "capacity",
    "structure": "stack",
    "cat-chem":"NMC111",
    "an-chem":"graphite",
    "capacity": 25, # Ah
    "anode_overhang": 1.08, # aus Warnecke2017
    "factor_more_capacity_cathode":1.55,
    "case_to_stack_layer_factor": 0.83,
    "h": 0.0265,  # Höhe oder Tiefe
    "l": 0.091,  # m BREITE
    "b": 0.148,  # m LÄNGE (2D hoehe)
    "b_jellyroll": 0.124,
    "ease_packaging_factor": 1.1,
    "D0": 0 * 10 ** -3,
    "casing_material": "Al",
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4, # Standardwert
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.8,
    #     "binder": 0.1,
    #     "carbon": 0.1
    # },
    "cat_activematerial": 0.8,
    "cat_binder": 0.1,
    "cat_conductivecarbon": 0.1,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.3, # Standardwert
    "an_porosity": 0.3, # Standardwert
    "cu" : 10 * 10**-6, # Werte aus Hettesheimer2017 für 2017
    "an" : 86 * 10**-6,
    "sep": 20 * 10**-6,
    "cat": 78 * 10**-6,
    "al" : 11 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 710
}
#####################################################################

########### Pouch cells #############################################
housing_thickness = 190 * 10**-6 # Pouchdicke Kovachev2019
pouch_fantasy1={ # pouch cell from Kovachev2019
    "name":"pouch_fantasy1",
    "type": "pouch",
    "design": None,
    "structure": "stack", #Kovachev2019
    "cat-chem":"NMC111", # Kovachev2019
    "an-chem":"graphite",
    "capacity": 41, # Ah Kovachev2019
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode":2, # Geschätzt aus Liebig2019
    "h": 7.7 * 10**-3, # TIEFE abmaße Mail Kovachev2019
    "l": 260 * 10**-3, #m LÄNGE
    "b": 215 * 10**-3 , #m BREITE (2D hoehe)
    "case_to_stack_layer_factor": 0.86, # mail Kovachev2019
    "housing_thickness": housing_thickness,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.2,
    "an_porosity": 0.3,
    "cu" : 10 * 10**-6, # Schichtdicken aus Kovachev2019
    "an" : 65 * 10**-6,
    "sep" :20 * 10**-6,
    "cat": 75 * 10**-6,
    "al" : 20 * 10**-6,
    "buffer" : 0 * 10**-6,
    "total_mass": 0
}

pouch_fantasy2={ # pouch cell from https://www.alibaba.com/product-detail/Li-PO-Battery-Cell-3-6v_62070177727.html?spm=a2700.galleryofferlist.0.0.45543a0aCUsljt
    "name":"pouch_fantasy2",
    "type": "pouch",
    "design": None,
    "structure": "stack",
    "cat-chem":"NMC111",
    "an-chem":"graphite",
    "capacity": 64, # Ah
    "anode_overhang": 1.1,
    "factor_more_capacity_cathode":1.5, # unklar
    "h": 11.5 * 10**-3, # TIEFE abmaße https://www.alibaba.com/product-detail/Original-NMC-L-G-Chem-e63_62151847686.html?spm=a2700.galleryofferlist.0.0.45543a0aCUsljt
    "l": 325 * 10**-3, #m LÄNGE
    "b": 134 * 10**-3 , #m BREITE (2D hoehe)
    "case_to_stack_layer_factor": 0.86, # mail Kovachev2019
    "housing_thickness": housing_thickness,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio":{
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.2,
    "an_porosity": 0.3,
    "cu" : 10 * 10**-6, # Schichtdicken aus Kovachev2019
    "an" : 65 * 10**-6,
    "sep" :20 * 10**-6,
    "cat": 75 * 10**-6,
    "al" : 20 * 10**-6,
    "total_mass": 0
}

Kokam_7_5AH={ # aus Ecker2015
    "name": "Kokam_7_5AH",
    "type": "pouch",
    "design": "allround",
    "structure": "stack",
    "cat-chem": "NC46",
    "an-chem": "graphite",
    "capacity": 7.5,  # Ah
    "anode_overhang": ((103)*(87))/ ((101)*(85)), # = 1.044 berechnet aus Ecker2015
    "factor_more_capacity_cathode": 1.16,  # nd
    "h": 7.9 * 10 ** -3, #
    "l": 102 * 10 ** -3,  #
    "b": 107 * 10 ** -3,  #
    "case_to_stack_layer_factor": ((103)*(87)) / (107*102), # =0.821,  # berechnet aus Ecker2015
    "housing_thickness": housing_thickness,
    "porosity_Separator": 0.58,
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.86,
    #     "binder": 0.07,
    #     "carbon": 0.07
    # },
    "cat_activematerial": 0.86,
    "cat_binder": 0.07,
    "cat_conductivecarbon": 0.07,
    "an_activematerial": 0.86,
    "an_binder": 0.07,
    "an_conductivecarbon": 0.07,
    "cat_porosity": 0.296,
    "an_porosity": 0.329,
    "cu": 14.7 * 10 ** -6,
    "an": 73.7 * 10 ** -6,
    "sep": 19 * 10 ** -6,
    "cat": 54.45 * 10 ** -6,
    "al": 15.11 * 10 ** -6,
    "total_mass": 165
}

EIG_ePLB_C020={ # Warnecke2017
    "name": "EIG_ePLB_C020",
    "type": "pouch",
    "design": "allround",
    "structure": "stack",
    "cat-chem": "NMC442",
    "an-chem": "graphite",
    "capacity": 20,  # Ah
    "anode_overhang": ((193.5-2)*(126-4))/ ((188.5-2)*(122-4)), #= 1.061, # berechnet aus Warnecke2017
    "factor_more_capacity_cathode": 1.16,  # nd
    "h": 7.2 * 10 ** -3, # Warnecke2017
    "l": 217 * 10 ** -3,  # m LÄNGE
    "b": 129 * 10 ** -3,  # m BREITE (2D hoehe)
    "an-l":193.5-2, #  Warnecke2017 the -2 and -4 define a cutout at the corners with a total of 8mm²=2mm*4mm
    "an-b": 126-4,
    "cat-l":188.5-2,
    "cat-b": 122-4,
    "case_to_stack_layer_factor": ((193.5-2)*(126-4)) / (217*129), # =0.83,  # berechnet aus Warnecke2017: surface case/ anode
    "housing_thickness": housing_thickness,
    "porosity_Separator": 0.408, # Warnecke2017
    "density_PP_PE": 0.95,  # g/cm³
    # "tape_am_binder_carbon_ratio": {
    #     "activematerial": 0.9,
    #     "binder": 0.05,
    #     "carbon": 0.05
    # },
    "cat_activematerial": 0.9,
    "cat_binder": 0.05,
    "cat_conductivecarbon": 0.05,
    "an_activematerial": 0.9,
    "an_binder": 0.05,
    "an_conductivecarbon": 0.05,
    "cat_porosity": 0.252, # Warnecke2017
    "an_porosity": 0.238, # Warnecke2017
    "cu": 10 * 10 ** -6,  # Schichtdicken aus Warnecke2017
    "an": 67 * 10 ** -6,
    "sep": 24.5 * 10 ** -6,
    "cat": 55 * 10 ** -6,
    "al": 20 * 10 ** -6,
    "total_mass": 428 #g aus Datenblatt online http://www.ebaracus.com/sites/default/files/2012/12/EIG-ePLB-C020-Datasheet.pdf
}
#####################################################################

all_cells = [samsung_25R, samsung_48G, samsung_30Q, A123, LG_HB4, LG_HB2, LG_HG2, sony_VTC6, sony_VTC5A, PHEV2, BEV2, Schmalstieg_pris, pouch_fantasy1, pouch_fantasy2, EIG_ePLB_C020, Kokam_7_5AH]