# Layers
# Kupfer cu
# Anode an
# Separator sep
# Cathode cat
# Aluminium al


# Cylindric cells
# Length spiral:
# https://www.giangrandi.org/soft/spiral/spiral.shtml

# prismatic / pouch

# Wickel-volume: length * width * height 

# choose chemistry --> get w./vol. percent

# APPROX. FORMULA. We look for L (length of the tape)
# geht the length(N,h,D0)
# L = pi*N*(D0 + h*(N-1))
#
# # get the N(h, D0, L)
# N = (h-D0+math.sqrt((D0-h)**2 + ((4*h*L)/(pi))))/(2*h)
#
# # get the D1(N,h,D0)
# D1 = 2*N*h + D0
#
# # get N(D1, D0, h)
# N = (D1-D0) / (2*h)








import math
import matplotlib.pyplot as plt
import numpy as np

DENSITY_ALUMINIUM = 2.7 # g/cm³
DENSITY_STEEL = 7.85 # g/cm³
DENSITY_COPPER = 8.96 # g/cm³

############################### Cells #####################################################
# Werte aus Lain2019
housing_thickness = 0.2
samsung_25R = {
    "name":"Samsung_25R",
    "type": "18650",
    "cat-chem":"NMC622",
    "an-chem":"graphit-si",
    "capacity": 2.57, # Ah
    "specific_capacity_paper": 0.179,  # Ah/g
    "D0":  4 * 10**-3,
    "D1": 18 * 10**-3,
    "l":  65 * 10**-3,
    "l_jellyroll": (60-housing_thickness)* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    "tape_am_binder_carbon_ratio":{
        "activematerial": 0.9,
        "binder": 0.05,
        "carbon": 0.05
    },
    "cat_porosity": 0.09,
    "an_porosity": 0.2,
    "cu" : 10 * 10**-6,
    "an" : 43 * 10**-6,
    "sep" :10 * 10**-6,
    "cat": 38 * 10**-6,
    "al" : 14 * 10**-6,
    "sep2" :10 * 10**-6,
    "buffer" : 0 * 10**-6
}

samsung_48G = {
    "name":"Samsung_48G",
    "type": "21700",
    "cat-chem":"NCA",
    "an-chem":"graphit-si",
    "capacity": 4.838, # Ah
    "specific_capacity_paper": 0.199,  # Ah/g
    "D0": 4 * 10**-3,
    "D1": 21 * 10**-3,
    "l":  70 * 10**-3,
    "l_jellyroll": (65-(housing_thickness))* 10**-3,
    "housing_thickness": housing_thickness* 10**-3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95, # g/cm³
    "tape_am_binder_carbon_ratio": {
        "activematerial": 0.9,
        "binder": 0.05,
        "carbon": 0.05
    },
    "cat_porosity": 0.13,
    "an_porosity": 0.22,
    "cu" : 10 * 10**-6,
    "an" : 85 * 10**-6,
    "sep" : 8 * 10**-6,
    "cat": 71 * 10**-6,
    "al" : 12 * 10**-6,
    "sep2" :8 * 10**-6,
    "buffer" : 0 * 10**-6
}

A123={
    "name":"A123",
    "type": "18650",
    "cat-chem": "LFP",
    "an-chem": "graphit",
    "capacity": 1.1,  # Ah
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    "tape_am_binder_carbon_ratio": {
        "activematerial": 0.9,
        "binder": 0.05,
        "carbon": 0.05
    },
    "cat_porosity": 0.26,
    "an_porosity": 0.25,
    "cu": 10 * 10 ** -6,
    "an": 36 * 10 ** -6,
    "sep": 18 * 10 ** -6,
    "cat": 81 * 10 ** -6,
    "al": 19 * 10 ** -6,
    "sep2": 18 * 10 ** -6,
    "buffer": 0 * 10 ** -6
}

LG_HB4={
    "name":"LG_HB4",
    "type": "18650",
    "cat-chem": "NMC111",
    "an-chem": "graphit",
    "capacity": 1.5,  # Ah
    "specific_capacity_paper": 0.133, #Ah/g
    "D0": 4 * 10 ** -3,
    "D1": 18 * 10 ** -3,
    "l": 65 * 10 ** -3,
    "l_jellyroll": (60 - 2 * housing_thickness) * 10 ** -3,
    "housing_thickness": housing_thickness * 10 ** -3,
    "porosity_Separator": 0.4,
    "density_PP_PE": 0.95,  # g/cm³
    "tape_am_binder_carbon_ratio": {
        "activematerial": 0.9,
        "binder": 0.05,
        "carbon": 0.05
    },
    "cat_porosity": 0.26,
    "an_porosity": 0.24,
    "cu": 15 * 10 ** -6,
    "an": 43 * 10 ** -6,
    "sep": 10 * 10 ** -6,
    "cat": 50 * 10 ** -6,
    "al": 25 * 10 ** -6,
    "sep2": 10 * 10 ** -6,
    "buffer": 0 * 10 ** -6
}
cell = LG_HB4
# cell= samsung_48G
cell=samsung_25R
##########################################################################################


############################### Conversions / Constants ##################################
# Cell-chemistry: NMC111, NMC622, NMC532, NMC811
# Electrical characteristics:
# NCA: 170-200 mAh/g
# NMC111: 160 mAh/g
# NMC532: 165 mAh/g
# NMC622: 170 mAh/g
# NMC811: 190 mAh/g

cathode_capacity_per_gram={
    "NCA": 0.185, # literature: 0.185Ah/g
    "NMC111": 0.160,
    "NMC532": 0.165,
    "NMC622": 0.170,
    "NMC811": 0.190,
    "LFP": 0.160
}

anode_capacity_per_gram={
    "graphit": 0.220, # Ah/g
    "graphit-si": 0.350 # Ah/g
}

cathode_densities={
    "LFP": 3.6, # g/cm³ Landesfeind2016
    "LNMO": 4.5, # g/cm³ Landesfeind2016
    "NMC111": 4.7, # g/cm³ Landesfeind2016
    "NMC811": 4.7, # g/cm³
    "NMC532": 4.7, # g/cm³
    "NMC622": 4.7, # g/cm³
    "NCA": 4.7, # g/cm³
    "LTO": 3.5 # g/cm³ Landesfeind2016
}

anode_densities={
    "graphite": 2.3 # g/cm³ Landesfeind2016
}

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
    }
}

def calculate_mass_percent_chemistry(chemistry):
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
            "pLi": am_Li/total_mass}
##########################################################################################



############################### Geometric calculations ###################################
D0 = cell["D0"] # inner diameter of the roll in m
D1_inside = cell["D1"] - 2 * cell["housing_thickness"] # outer diameter of roll in m
#h = 0.1 * 10⁻3 # total thickness of the the tape in m
# h version 1
#h = cell["cu"]+cell["an"]+cell["sep"]+cell["cat"]+cell["al"]+cell["sep2"]+cell["buffer"] # total thickness of tape

# h version 2
h = cell["sep"]+cell["an"]+cell["cu"]+cell["an"]+cell["sep"]+cell["cat"]+cell["al"]+cell["cat"]
ease_packaging_factor = 1.05
N = (D1_inside - D0) / (2 * h*ease_packaging_factor)
L_tape = math.pi * N * (D0 + h * (N - 1))

# surface cathode
anode_overhang = 0.9
scat = anode_overhang* L_tape * cell["l_jellyroll"]*2

# volume cathode:
vc = scat*cell["cat"] # m³

# surface anode
s_anode = L_tape * cell["l_jellyroll"]*2

# volume anode
va = s_anode*cell["an"]

print(cell["name"])
print("* Doing the geometric calculations, based on the thickness od the layers.")
print("Turns: {turns:.2f}, length: {length:.2f} m, surface tape: {st:.3f} m², surface cat: {scat:.3f} m²"
      " volume wickel: {vw:.2f} cm³, volume cat: {vc:.2f} cm³,"
      " volume cell body: {vcb:.2f} cm³, h: {h:.2f} mm".format(turns=N, length=L_tape, st=L_tape * cell["l_jellyroll"],
                                                               scat=scat,
                                                               vw=(L_tape * cell["l_jellyroll"] * h) * 1000000,
                                                               vc=vc * 1000000,
                                                               vcb=(cell["l"]*((cell["D1"]/2)**2)*math.pi)*1000000, h=h*1000))
##########################################################################################




############################### Masses via Ah/g-relationship #############################
# Cathode Active Material
# calculate the mass of the cat-material via the Ah/g-relationship:
if "specific_capacity_paper" in cell:
    cap_per_gram = cell["specific_capacity_paper"]
else:
    cap_per_gram = cathode_capacity_per_gram[cell["cat-chem"]]

mass_cat_material = cell["capacity"] / cap_per_gram
shares = calculate_mass_percent_chemistry(cell["cat-chem"])

# Get the shares of the cathode tape mixture am/binder/C --> 90%/5%/5%
mass_active_cat_material = mass_cat_material * cell["tape_am_binder_carbon_ratio"]["activematerial"]

# Get the shares of the single objects
mLi = shares["pLi"]*mass_active_cat_material
mNi = shares["pNi"]*mass_active_cat_material
mMn = shares["pMn"]*mass_active_cat_material
mCo = shares["pCo"]*mass_active_cat_material
mAl = shares["pAl"]*mass_active_cat_material
mFe = shares["pFe"]*mass_active_cat_material
mP = shares["pP"]*mass_active_cat_material

print("* Mass calculation of active materials through the capacity/g entity from the cell-manufacturers data sheet:")
print("Cathode material total: {mtotal:.2f} g. active cat material: {macm:.2f} g, Li: {mli:.2f} g, Ni: {mni:.2f} g, Mn: {mmn:.2f} g, Co: {mco:.2f} g, Al: {mal:.2f} g, Fe: {mfe:.2f} g, P: {mp:.2f} g".format(mtotal=mass_cat_material, macm=mass_active_cat_material, mli=mLi, mni=mNi, mmn=mMn, mco=mCo, mal = mAl, mfe=mFe, mp=mP))

# calculate the Volume and the density of the cathode
vol_cat = vc
cat_porosity = cell["cat_porosity"]
vol_cat_without_porosity = (1-cat_porosity)*vol_cat
density_active_cat = mass_active_cat_material/(vol_cat_without_porosity*1000000) # g/cm^3
print("Calculated density of the cathode active material: {dens_cat:.2f} g/cm³, "
      "vol cat: {vol_cat:.2f} cm³, vol cat without porosity: {vol_cat_without_porosity:.2f} cm³".format(dens_cat=density_active_cat,
                                                                                                   vol_cat=vol_cat*1000000,
                                                                                                   vol_cat_without_porosity=vol_cat_without_porosity*1000000))
# Anode Active Material
# calculate the mass of the anode
cap_per_gram = anode_capacity_per_gram[cell["an-chem"]]
mass_an_material = cell["capacity"] / cap_per_gram
print("Anode active material total: {mantotal:.2f} g.".format(mantotal=mass_an_material))

# calculate the density of the anode
an_porosity=cell["an_porosity"]
density_active_an = mass_an_material/((1-an_porosity) * va*1000000) # g/cm^3
print("Calculated density of the anode active material: {dens_an:.2f} g/cm³".format(dens_an=density_active_an))
##########################################################################################









################################### Masses of inactive parts ################################
# Mass of copper and aluminium in the collectors
# Round Cell
mAl_collector = ((L_tape * cell["al"] * cell["l_jellyroll"]) * 1000000) * DENSITY_ALUMINIUM # g
mCu_collector = ((L_tape * cell["cu"] * cell["l_jellyroll"]) * 1000000) * DENSITY_COPPER # g

print("* Mass calculation for aluminium and copper through the geometric estimation:")
print("Aluminium in collector: {mAl_collector:.2f} g, Copper in collector: {mCu_collector:.2f} g".format(mAl_collector=mAl_collector, mCu_collector=mCu_collector))

# Mass calculation of separator
vSeparator = L_tape * (cell["sep"] + cell["sep2"]) * cell["l_jellyroll"] * 1000000 # cm³
mSep = cell["density_PP_PE"]*cell["porosity_Separator"]*vSeparator # g
print("Mass of separator: {mSep:.2f} g".format(mSep=mSep))

# Mass of the casing of the cell
# Round Cell
vCasing = ((((cell["D1"]/2)**2)*math.pi*cell["housing_thickness"])*2 + 2*math.pi*(cell["D1"]/2) * cell["l"] * cell["housing_thickness"]) * 1000000
mSteelCasing = DENSITY_STEEL * vCasing
print("* Mass calculation of the casing. Material of case: steel. geometric.")
print("Steel in casing: {mSteelCasing:.2f} g.".format(mSteelCasing=mSteelCasing))

# Total mass
print("* Total mass of cell without electrolyte: {massCell:.2f} g".format(massCell=mSteelCasing + mSep + mAl_collector + mCu_collector + mass_cat_material + mass_an_material))
##########################################################################################




############ Plot the cell #################################################
# h+=0.00005
f = plt.figure(figsize=(12,12))
res = 9000
N = (D1_inside - D0) / (2 * h)
theta = np.linspace(0, N*2*math.pi, res)


s1 = cell["sep"]
s2 = cell["sep"] + cell["an"]
s3 = cell["sep"] + cell["an"] + cell["cu"]
s4 = cell["sep"] + cell["an"] + cell["cu"] + cell["an"]
s5 = cell["sep"] + cell["an"] + cell["cu"] + cell["an"]+cell["sep"]
s6 = cell["sep"] + cell["an"] + cell["cu"] + cell["an"]+cell["sep"] + cell["cat"]
s7 = cell["sep"] + cell["an"] + cell["cu"] + cell["an"]+cell["sep"] + cell["cat"]+cell["al"]
s8 = cell["sep"] + cell["an"] + cell["cu"] + cell["an"]+cell["sep"] + cell["cat"]+cell["al"]+cell["cat"]

r       = np.linspace((D0/2),    (D1_inside / 2) - h, res)
r_sep1  = np.linspace((D0/2)+s1, (D1_inside / 2) - h+s1, res)
r_an1   = np.linspace((D0/2)+s2, (D1_inside / 2) - h+s2, res)
r_cu    = np.linspace((D0/2)+s3, (D1_inside / 2) - h+s3, res)
r_an2   = np.linspace((D0/2)+s4, (D1_inside / 2) - h+s4, res)
r_sep2  = np.linspace((D0/2)+s5, (D1_inside / 2) - h+s5, res)
r_cat1  = np.linspace((D0/2)+s6, (D1_inside / 2) - h+s6, res)
r_al    = np.linspace((D0/2)+s7, (D1_inside / 2) - h+s7, res)
r_cat2  = np.linspace((D0/2)+s8, (D1_inside / 2) - h+s8, res)

# r_ = np.linspace((D0/2)+s8, (D1_inside / 2) - h+s8, res)
# r_cu = np.linspace((D0/2) + cell["cu"], (D1_inside / 2) - h + cell["cu"], res)
# r_an = np.linspace((D0/2) + cell["cu"] + cell["an"], (D1_inside / 2) - h + cell["cu"] + cell["an"], res)
# r_sep = np.linspace((D0/2) + cell["cu"] + cell["an"] + cell["sep"], (D1_inside / 2) - h + cell["cu"] + cell["an"] + cell["sep"], res)
# r_cat = np.linspace((D0/2) + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"], (D1_inside / 2) - h + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"], res)
# r_al = np.linspace((D0/2) + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"] + cell["al"], (D1_inside / 2) - h + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"] + cell["al"], res)
# r_sep2 = np.linspace((D0/2) + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"] + cell["al"] + cell["sep2"], (D1_inside / 2), res)
# Plot wickel
plt.polar(theta, r, label="baseline", linewidth=0)
plt.polar(theta, r_sep1, label="sep", linewidth=0)
plt.fill_between(theta, r, r_sep1, facecolor="black")
#
plt.polar(theta, r_an1, label="an", linewidth=0)
plt.fill_between(theta, r_sep1, r_an1, facecolor="red")
#
plt.polar(theta, r_cu, label="cu", linewidth=0)
plt.fill_between(theta, r_an1, r_cu, facecolor="gold")
#
plt.polar(theta, r_an2, label="an", linewidth=0)
plt.fill_between(theta, r_cu, r_an2, facecolor="red")
#
plt.polar(theta, r_sep2,label="sep2", linewidth=0)
plt.fill_between(theta, r_an2, r_sep2, facecolor="black")
#
plt.polar(theta, r_cat1, label="cat", color="blue", linewidth=0)
plt.fill_between(theta, r_sep2, r_cat1, facecolor="blue")

plt.polar(theta, r_al, label="al", color="silver", linewidth=0)
plt.fill_between(theta, r_cat1, r_al, facecolor="silver")

plt.polar(theta, r_cat2, label="cat", color="blue", linewidth=0)
plt.fill_between(theta, r_al, r_cat2, facecolor="blue")
##################################
# Caseing
circle=np.linspace(0,2*math.pi,res)
r_case1=[(cell["D1"]/2) - cell["housing_thickness"] ]*res
r_case2=[(cell["D1"]/2)+ cell["housing_thickness"]  ]*res
plt.polar(circle, r_case1, label="case",color='black')
plt.polar(circle, r_case2,color='black')
plt.fill_between(circle, r_case1, r_case2, facecolor='grey', hatch = "/////")
plt.legend()
plt.xlim([0,2*math.pi])
plt.ylim([0.0018,0.0024])
# plt.ylim([0.009,0.011])
# plt.show()