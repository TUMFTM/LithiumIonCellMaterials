'''
This file contains constants and conversions
'''

DENSITY_ALUMINIUM = 2.7 # g/cm³
DENSITY_STEEL = 7.85 # g/cm³
DENSITY_COPPER = 8.96 # g/cm³

DENSITY_CONDUCTIVE_CARBON = 1.5 # g/cm³ https://en.wikipedia.org/wiki/Carbon_black
DENSITY_PVDF_BINDER = 1.77 # g/cm³ https://de.wikipedia.org/wiki/Polyvinylidenfluorid

# Cell-chemistry: NMC111, NMC622, NMC532, NMC811
# Electrical characteristics:
# NCA: 170-200 mAh/g
# NMC111: 160 mAh/g
# NMC532: 165 mAh/g
# NMC622: 170 mAh/g
# NMC811: 190 mAh/g

general_materials_density = {
    "steel": DENSITY_STEEL,
    "Al": DENSITY_ALUMINIUM,
    "Cu": DENSITY_COPPER
}

cathode_capacity_per_gram={
    "NCA": 0.190, # literature: 0.185Ah/g Doeff2012
    "NMC111": 0.165,
    "NC46": 0.165, # NICHT BELEGT
    "NMC442": 0.165, # NICHT BELEGT
    "NMC532": 0.165,
    "NMC622": 0.170,
    "NMC811": 0.190,
    "LFP": 0.160,
    "NCA+NMC622":(0.185+0.170)/2
}

anode_capacity_per_gram={
    "graphite": 0.22, # Ah/g
    "graphite-si": 0.350 # Ah/g
}

# Schüttdichte oder tap-dichte aus landesfeind2016
cathode_active_densities={
    "LFP": 3.6, # g/cm³ 3.6 Landesfeind2016
    "LNMO": 4.5, # g/cm³ Landesfeind2016
    "NMC111": 4.7, # g/cm³ Landesfeind2016
    "NC46": 4.75, # g/cm³ Ecker2015
    "NMC811": 4.7, # g/cm³
    "NMC532": 4.7, # g/cm³
    "NMC622": 4.7, # g/cm³
    "NMC442": 4.7, # g/cm³ NICHT BELEGT
    "NCA": 4.7, # g/cm³
    "LTO": 3.5, # g/cm³ Landesfeind2016
    "NCA+NMC622":(4.7+4.7)/2 # g/cm³ mix
}

# Verarbeitete densities aus Zheng2017
# Pressed densities on tape
cathode_densities={
    "LFP": 2.3, # g/cm³ Zheng2017
    "LNMO": 4.5, # g/cm³ Landesfeind2016
    "NMC111": 3.4, # g/cm³ Zheng2017
    "NMC811": 3.2, # g/cm³ Zheng2017
    "NMC532": 3.3, # g/cm³ geraten
    "NMC622": 3.3, # g/cm³ geraten
    "NCA": 3.4, # g/cm³ Zheng2017
    "LMO": 3.2, # g/cm³ Zheng2017
    "NCA+NMC622":(3.4+3.3)/2 # g/cm³ mix
}

anode_active_densities={
    "graphite": 2.3,  # g/cm³ Landesfeind2016 2.1-2.3 g/cm³ in https://de.wikipedia.org/wiki/Graphit#cite_note-HollemanWiberg-4
    "graphite-si": 2.3  # g/cm³ NO SOURCE
}

anode_densities={
    "graphite": 2.3, # g/cm³ Landesfeind2016 2.1-2.3 g/cm³ in https://de.wikipedia.org/wiki/Graphit#cite_note-HollemanWiberg-4
    "graphite-si": 2.3 # g/cm³ NO SOURCE
}
# anode_densities={
#     "graphite": 1.75, # g/cm³ Meyer2017
#     "graphite-si": 1.75 # g/cm³ NO SOURCE
# }

cell_chemistry_shares={
    "NCA": {
        "N":0.8,
        "C":0.15,
        "A":0.05,
        "O":2
    },
    "NMC111": {
        "N":0.33,
        "M":0.33,
        "C":0.33,
        "O":2
    },
    "NMC442": {
        "N":0.4,
        "M":0.4,
        "C":0.2,
        "O":2
    },
    "NMC532": {
        "N":0.5,
        "M":0.3,
        "C":0.2,
        "O":2
    },
    "NMC622": {
        "N":0.6,
        "M":0.2,
        "C":0.2,
        "O":2
    },
    "NMC811": {
        "N":0.8,
        "M":0.1,
        "C":0.1,
        "O":2
    },
    "LFP":{
        "F":1,
        "P":1,
        "O":4
    },
    "NCA+NMC622":{
        "N":(0.6+0.8)/2,
        "M":0.2,
        "C":(0.2+0.15)/2,
        "A": 0.05,
        "O": 2
    },
    "NC46":{
        "N":0.4,
        "C":0.6,
        "O":2
    }
}

def theoretical_capacity(cell, geometric):
    '''
    Ctheo = (ρ · V · F) / M
    '''
    F = 9.648533212331*10**4 # As/mol

    # Cathode
    M = calculate_mass_percent_chemistry(cell["cat-chem"])["total_molar_mass"] #kg/mol
    roh = 1000*cathode_active_densities[cell["cat-chem"]] # kg/m³

    # Volume
    vol_cat = geometric["volume_cathode"]
    cat_porosity = cell["cat_porosity"]
    vol_cat_without_porosity = (1 - cat_porosity) * vol_cat
    vol_active_cat_without_porosity = vol_cat_without_porosity * (
                (cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]]) / (
                    cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]] +
                    cell["cat_binder"] / DENSITY_PVDF_BINDER + cell["cat_conductivecarbon"] / DENSITY_CONDUCTIVE_CARBON))

    C_theo_cat = (roh * vol_cat * F) / M #As
    C_theo_cat_Ah = C_theo_cat/3600 # Ah

    C_total_cat = (roh * vol_active_cat_without_porosity * F) / M #As
    C_total_cat_Ah = C_total_cat/3600 # Ah


    # Anode
    M = 6*12/1000 # kg/mol
    roh = 1000 * anode_active_densities[cell["an-chem"]] # kg/m³
    vol_an = geometric["volume_anode"] # m³
    an_porosity = cell["an_porosity"]
    vol_an_without_porosity = (1 - an_porosity) * vol_an
    vol_active_an_without_porosity = vol_an_without_porosity * (
            (cell["an_activematerial"] / anode_active_densities[cell["an-chem"]]) / (
            cell["an_activematerial"] / anode_active_densities[cell["an-chem"]] +
            cell["an_binder"] / DENSITY_PVDF_BINDER + cell["an_conductivecarbon"] / DENSITY_CONDUCTIVE_CARBON))

    C_theo_an = (roh * vol_an * F) / M  # As
    C_theo_an_Ah = C_theo_an / 3600 # Ah

    C_total_an = (roh * vol_active_an_without_porosity * F) / M #As
    C_total_an_Ah = C_total_an/3600 # Ah

    return {"C_theo_cat_Ah": C_theo_cat_Ah,
            "C_total_cat": C_total_cat_Ah,
            "C_total_an": C_total_an_Ah,
            "C_theo_an_Ah": C_theo_an_Ah}



def calculate_mass_percent_chemistry(chemistry):
    N_A = 6.02214076*10**23 # Avogadro Konstante: 1/mol

    #Atomic masses
    am_Li = 6.941 #u
    am_Ni = 58.6 #u
    am_Mn = 54.93 #u
    am_Co = 58.93 #u
    am_O  = 16 #u
    am_Al = 26.98 #u
    am_Fe = 55.85#u
    am_P=  30.97#u

    shares = cell_chemistry_shares[chemistry]

    total_mass = am_Li
    mNi = 0
    mMn = 0
    mCo = 0
    mAl = 0
    mFe=0
    mP=0
    for k,v in shares.items():
        if k == "N":
            mNi = am_Ni*v
            total_mass = total_mass + am_Ni * v
        if k == "M":
            mMn = am_Mn * v
            total_mass = total_mass + am_Mn * v
        if k == "C":
            mCo = am_Co * v
            total_mass = total_mass + am_Co * v
        if k == "A":
            mAl = am_Al * v
            total_mass = total_mass + am_Al * v
        if k == "O":
            mO = am_O * v
            total_mass = total_mass + am_O * v
        if k == "F":
            mFe = am_Fe * v
            total_mass = total_mass + am_Fe * v
        if k == "P":
            mP = am_P * v
            total_mass = total_mass + am_P * v

    return {"pNi": mNi/total_mass,
            "pMn": mMn/total_mass,
            "pCo": mCo/total_mass,
            "pAl": mAl/total_mass,
            "pFe": mFe/total_mass,
            "pP":  mP/total_mass,
            "pO":  mO/total_mass,
            "pLi": am_Li/total_mass,
            "total_molar_mass":total_mass*N_A*1.66*10**-27} # atommassen * Avogadro * Faktor_u_to_Kg


def mass_percent_to_volume_percent(wt1, dense1, wts, denses):

    assert len(wts) == len(denses)

    total_vol = 0
    for i in range(0, len(wts)):
        total_vol = total_vol + (wts[i] / denses[i])

    volume_percent_1 = (wt1/dense1) / total_vol

    return volume_percent_1