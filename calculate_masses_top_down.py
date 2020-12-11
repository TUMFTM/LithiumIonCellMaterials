
from util import DENSITY_COPPER, DENSITY_ALUMINIUM, DENSITY_STEEL, calculate_mass_percent_chemistry

def calculate_masses_top_down(cell, **kwargs):

    # use kwargs first, then look into cell
    if "total_mass" in kwargs:
        mass = kwargs["total_mass"]
    else:
        mass = cell["total_mass"]

    # shares from paper Velazquez-Martinez2019
    p_case = 0.25
    p_cathode= 0.27
    p_anode = 0.17
    p_collectors = 0.13
    p_electrolyte = 0.1
    p_sep = 0.04
    p_binder=0.04

    # case
    mass_case = mass * p_case

    # electrolyte
    mass_electrolyte = mass*p_electrolyte

    # sep
    mass_sep = mass * p_sep

    # binder
    mass_binder = mass*p_binder

    # anode
    mass_anode = mass*p_anode

    # cathode
    mass_cathode = mass * p_cathode
    mass_active_cat_material = mass_cathode * cell["cat_activematerial"]

    shares_cathode = calculate_mass_percent_chemistry(cell["cat-chem"])
    mLi = shares_cathode["pLi"] * mass_active_cat_material
    mNi = shares_cathode["pNi"] * mass_active_cat_material
    mMn = shares_cathode["pMn"] * mass_active_cat_material
    mCo = shares_cathode["pCo"] * mass_active_cat_material
    mAl = shares_cathode["pAl"] * mass_active_cat_material
    mFe = shares_cathode["pFe"] * mass_active_cat_material
    mP = shares_cathode["pP"] * mass_active_cat_material

    print("* Mass calculation Top Down. Given cell mass: {mass:.2f} g".format(mass=mass))
    print("Active cat material: {macm:.2f} g, Li: {mli:.2f} g, Ni: {mni:.2f} g, Mn: {mmn:.2f} g, Co: {mco:.2f} g, Al: {mal:.2f} g, Fe: {mfe:.2f} g, P: {mp:.2f} g".format(macm=mass_cathode, mli=mLi, mni=mNi, mmn=mMn, mco=mCo, mal = mAl, mfe=mFe, mp=mP))
    print("Mass case: {mass_case:.2f} g. Mass separator {mass_sep:.2f} g. Mass electrolyte {mass_ele:.2f} g".format(mass_case=mass_case, mass_sep=mass_sep, mass_ele=mass_electrolyte))

    return {"mass_cat_material": mass_cathode,
            "mass_active_cat_material": mass_active_cat_material,
            "mass_an_material": mass_anode,
            "mass_sep": mass_sep,
            "mass_binder": mass_binder,
            "mass_electrolyte": mass_electrolyte,
            "mass_case": mass_case,
            "mLi": mLi,
            "mNi": mNi,
            "mMn": mMn,
            "mCo": mCo,
            "mAl": mAl,
            "mFe": mFe,
            "mP": mP
            }