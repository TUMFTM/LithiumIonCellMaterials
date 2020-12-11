'''
This file contains the calculation of masses of inactive materials of the cell
Separator
Anode-collector
Cathode-collector
Casing

and contains the function for calculating the total mass
'''
from util import DENSITY_STEEL, DENSITY_ALUMINIUM, DENSITY_COPPER, general_materials_density
import math

def __calculate_prismatic_terminals(cell):
    # Terminal height: 6-8 mm. avg. 7# DIN91252
    h_avg = 7
    # Terminal width: 9-18 mm.
    w_avg = 13.5
    # Terminal length: 24-28 mm
    l_avg = 26

    if "terminal_type" in cell:
        if cell["terminal_type"] == "round":
            d_terminal = cell["d_terminal"]
            h_terminal = cell["h_terminal"]
            vol_terminal = math.pi * (d_terminal/2)**2 * h_terminal # mm³


        if cell["terminal_type"] == "square":
            w_terminal = cell["w_terminal"]
            l_terminal = cell["l_terminal"]
            h_terminal = cell["h_terminal"]
            vol_terminal = w_terminal * l_terminal * h_terminal # mm³

    else:
        # Use averages from above
        vol_terminal = h_avg*w_avg*l_avg # mm³


    mass_terminal = (vol_terminal/1000) * DENSITY_STEEL
    mass_terminals = 2 * mass_terminal
    return mass_terminals




def __calculate_masses_inactive_cylindric(cell, geometry_calculations):
    L_tape = geometry_calculations["L_tape"]

    # Mass of copper and aluminium in the collectors
    # Round Cell
    mAl_collector = ((L_tape * cell["al"] * cell["l_jellyroll"]) * 1000000) * DENSITY_ALUMINIUM  # g
    mCu_collector = ((L_tape * cell["cu"] * cell["l_jellyroll"]) * 1000000) * DENSITY_COPPER  # g

    print("* Mass calculation for aluminium and copper through the geometric estimation:")
    print("Aluminium in collector: {mAl_collector:.2f} g, Copper in collector: {mCu_collector:.2f} g".format(
        mAl_collector=mAl_collector, mCu_collector=mCu_collector))

    # Mass calculation of separator
    vSeparator = L_tape * (cell["sep"] + cell["sep2"]) * cell["l_jellyroll"] * 1000000  # cm³
    mSep = cell["density_PP_PE"] * cell["porosity_Separator"] * vSeparator  # g
    print("Mass of separator: {mSep:.2f} g".format(mSep=mSep))

    # Mass of the casing of the cell
    # Round Cell
    vCasing = ((((cell["D1"] / 2) ** 2) * math.pi * cell["housing_thickness"]) * 2 + 2 * math.pi * (cell["D1"] / 2) *
               cell["l"] * cell["housing_thickness"]) * 1000000
    mSteelCasing = DENSITY_STEEL * vCasing
    print("* Mass calculation of the casing. Material of case: steel. geometric.")
    print("Steel in casing: {mSteelCasing:.2f} g.".format(mSteelCasing=mSteelCasing))

    return {"mAl_collector": mAl_collector,
            "mCu_collector": mCu_collector,
            "mSep": mSep,
            "mCasing": mSteelCasing,
            "mass_terminals": 0}

def __calculate_masses_inactive_prismatic(cell, geometry_calculations):


    surface_cathode = geometry_calculations["surface_cathode"] / 2 # current collector is not double coated, hence by 2
    surface_anode = geometry_calculations["surface_anode"] / 2 # current collector is not double coated, hence by 2
    volume_separator = geometry_calculations["volume_separator"]

    # Mass of copper and aluminium in the collectors
    mAl_collector = ((surface_cathode * cell["al"]) * 1000000) * DENSITY_ALUMINIUM  # g
    mCu_collector = ((surface_anode * cell["cu"]) * 1000000) * DENSITY_COPPER  # g

    print("* Mass calculation for aluminium and copper through the geometric estimation:")
    print("Aluminium in collector: {mAl_collector:.2f} g, Copper in collector: {mCu_collector:.2f} g".format(
        mAl_collector=mAl_collector, mCu_collector=mCu_collector))

    # Mass calculation of separator
    vSeparator = volume_separator * 1000000  # cm³
    mSep = cell["density_PP_PE"] * cell["porosity_Separator"] * vSeparator  # g
    print("Mass of separator: {mSep:.2f} g".format(mSep=mSep))

    # Mass of the casing of the cell
    V_casing_outside = cell["l"] * cell["b"] * cell["h"]
    V_casing_inside = (cell["l"]-2*cell["housing_thickness"]) * (cell["b"]-2*cell["housing_thickness"]) * (cell["h"]-2*cell["housing_thickness"])
    V_casing = V_casing_outside-V_casing_inside

    if "casing_material" in cell:
        casing_density = general_materials_density[cell["casing_material"]]
        case_material = cell["casing_material"]
    else:
        casing_density = DENSITY_STEEL
        case_material = "steel"

    mSteelCasing = casing_density*1000000 * V_casing
    print("* Mass calculation of the casing. Material of case: {}. geometric.".format(case_material))
    print("Steel in casing: {mSteelCasing:.2f} g.".format(mSteelCasing=mSteelCasing))

    # Mass Terminals
    mass_terminals = __calculate_prismatic_terminals(cell)
    print("* Mass calculation of the terminals")
    print(f"Mass of terminals: {round(mass_terminals, 2)} g")

    return {"mAl_collector": mAl_collector,
            "mCu_collector": mCu_collector,
            "mSep": mSep,
            "mCasing": mSteelCasing,
            "mass_terminals": mass_terminals}

def __calculate_masses_inactive_pouch(cell, geometry_calculations):

    surface_cathode = geometry_calculations["surface_cathode"] / 2 # its not double coated, hence by 2
    surface_anode = geometry_calculations["surface_anode"] / 2 # its not double coated, hence by 2
    volume_separator = geometry_calculations["volume_separator"]

    # Mass of copper and aluminium in the collectors
    mAl_collector = ((surface_cathode * cell["al"]) * 1000000) * DENSITY_ALUMINIUM  # g
    mCu_collector = ((surface_anode * cell["cu"]) * 1000000) * DENSITY_COPPER  # g

    print("* Mass calculation for aluminium and copper through the geometric estimation:")
    print("Aluminium in collector: {mAl_collector:.2f} g, Copper in collector: {mCu_collector:.2f} g".format(
        mAl_collector=mAl_collector, mCu_collector=mCu_collector))

    # Mass calculation of separator
    vSeparator = volume_separator * 1000000  # cm³
    mSep = cell["density_PP_PE"] * cell["porosity_Separator"] * vSeparator  # g
    print("Mass of separator: {mSep:.2f} g".format(mSep=mSep))

    # Mass of the casing of the cell
    V_casing_outside = cell["l"] * cell["b"] * cell["h"]
    V_casing_inside = (cell["l"]-2*cell["housing_thickness"]) * (cell["b"]-2*cell["housing_thickness"]) * (cell["h"]-2*cell["housing_thickness"])
    V_casing = V_casing_outside-V_casing_inside
    mAluCasing = DENSITY_ALUMINIUM*1000000 * V_casing
    print("* Mass calculation of the casing. Material of case: Alu compound. geometric.")
    print("Alu in casing: {mAluCasing:.2f} g.".format(mAluCasing=mAluCasing))

    return {"mAl_collector": mAl_collector,
            "mCu_collector": mCu_collector,
            "mSep": mSep,
            "mCasing": mAluCasing,
            "mass_terminals": 0}

def calculate_masses_inactive(cell, geometry_calculations):
    inactive_masses=None

    if cell["type"] == "18650" or cell["type"] == "21700":
        inactive_masses = __calculate_masses_inactive_cylindric(cell, geometry_calculations)

    if cell["type"] == "prismatic":
        inactive_masses = __calculate_masses_inactive_prismatic(cell, geometry_calculations)

    if cell["type"] == "pouch":
        inactive_masses= __calculate_masses_inactive_pouch(cell, geometry_calculations)


    return inactive_masses

def calculate_total_mass(inactive, active, cell, geometry_calculations):
    # INPUT: mSteelCasing, mSep, mAl_collector, mCu_collector, mass_cat_material, mass_an_material)
    mSteelCasing = inactive["mCasing"]
    mSep = inactive["mSep"]
    mAl_collector = inactive["mAl_collector"]
    mCu_collector = inactive["mCu_collector"]
    mass_cat_material = active["mass_cat_material"]
    mass_an_material = active["mass_an_material"]

    if "mass_terminals" in inactive:
        mass_terminals = inactive["mass_terminals"]
    else:
        mass_terminals=0

    # Total mass
    total_mass_wo_electrolyte = mass_terminals + mSteelCasing + mSep + mAl_collector + mCu_collector + mass_cat_material + mass_an_material


    # Mass of electrolyte:
    cp = cell["cat_porosity"]
    ap = cell["an_porosity"]
    ps = cell["porosity_Separator"]

    cv = geometry_calculations["volume_cathode"]
    av = geometry_calculations["volume_anode"]
    sv = geometry_calculations["volume_separator"]

    vol_electrolyte = cp*cv*1000000 + ap*av*1000000 + ps*sv*1000000
    mass_electrolyte = vol_electrolyte * 0.95 #g/cm³ #Wu2016

    total_mass = total_mass_wo_electrolyte+mass_electrolyte
    print("* Total mass of cell without electrolyte: {massCell:.2f} g. Mass electrolyte: {mass_ele:.2f} g".format(massCell=total_mass_wo_electrolyte, mass_ele=mass_electrolyte))
    print("* Total mass of cell: {massCell:.2f} g".format(massCell=total_mass))




    return {
        "total_mass": total_mass,
        "mass_electrolyte": mass_electrolyte
    }
