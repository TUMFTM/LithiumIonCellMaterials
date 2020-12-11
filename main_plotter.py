from cells import PHEV2, pouch_fantasy1, pouch_fantasy2, BEV2, samsung_48G, samsung_25R, LG_HB4, A123, Schmalstieg_pris
from geometric import geometric_calculation
from calculate_masses_ah_g import calculate_masses_ah_g
from calculate_masses_density_based import calculate_masses_density_based
from calculate_masses_inactive import calculate_masses_inactive, calculate_total_mass
from calculate_masses_top_down import calculate_masses_top_down
import matplotlib.pyplot as plt
import numpy as np
import copy
import util
########################### helper ########################################
def plot_elements(axs, cell, masses, marker, postfix, legend_entries):
    flag_legend_elements=0
    elements = ["mLi", "mNi", "mMn", "mCo", "mAl", "mFe", "mP"]
    colors =   ["orange", "blue", "green", "red", "coral", "gray", "fuchsia"]

    for idx, ele in enumerate(elements):
        if masses[ele] > 0:
            axs.plot(cell["name"], masses[ele], markersize=7, marker=marker, label=ele+postfix if ele+postfix not in legend_entries else "", color=colors[idx])
            legend_entries.append(ele+postfix)

    return legend_entries
    # print(legend_entries)

def calculate_cell(cell):
    gc = geometric_calculation(cell)
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

    return inactive_masses, mass_ahg, total_mass_ah_g, masses_density, total_mass_density, total_mass, mass_topdown, gc
###########################################################################
cells = [PHEV2, BEV2, pouch_fantasy1, pouch_fantasy2, samsung_48G, samsung_25R, LG_HB4, A123, Schmalstieg_pris]



################# Manual Test ########################################
cell_v = copy.copy(cells[4])
cell_v["anode_overhang"]=1.1 # 0.1-0.2
cell_v["cat_porosity"]=0.1 # 0.1-0.3

cell_v["factor_more_capacity_cathode"]=1 # 1-2
DENSITY_LIT = 4.4 #4.7 #3.6 # 4.7

print("--------")
print("* Run 1 ----------------------------------------------------------------------")
spec_capa = util.cathode_capacity_per_gram[cell_v["cat-chem"]]
inactive_masses, mass_ahg, total_mass_ah_g, masses_density, total_mass_density, total_mass, mass_topdown, gc = calculate_cell(cell_v)
Cf = (DENSITY_LIT* gc["volume_cathode"]*1000000 * (1-cell_v["cat_porosity"]) * spec_capa*cell_v["cat_activematerial"])/cell_v["capacity"]

print("--------")
print("* Run 2 ----------------------------------------------------------------------")
cell_v["factor_more_capacity_cathode"]=Cf # 1-2
inactive_masses, mass_ahg, total_mass_ah_g, masses_density, total_mass_density, total_mass, mass_topdown, gc = calculate_cell(cell_v)

print("------------------------------------------------------------------------------")
print("-----------------##---------V2-----------##-------------------##--------------")
print("------------------------------------------------------------------------------")

print("--------")
print("* Run 1 ----------------------------------------------------------------------")
cell_v["anode_overhang"]=1.2 # 0.1-0.2
cell_v["cat_porosity"]=0.3 # 0.1-0.3
inactive_masses2, mass_ahg2, total_mass_ah_g2, masses_density2, total_mass_density2, total_mass2, mass_topdown2, gc2 = calculate_cell(cell_v)
spec_capa = util.cathode_capacity_per_gram[cell_v["cat-chem"]] #cell_v["specific_capacity_paper"]

Cf2 = (DENSITY_LIT* gc2["volume_cathode"]*1000000 * (1-cell_v["cat_porosity"])*spec_capa*cell_v["cat_activematerial"])/cell_v["capacity"]
print("--------")
print("* Run 2 ----------------------------------------------------------------------")
cell_v["factor_more_capacity_cathode"]=Cf2 # 1-2
inactive_masses2, mass_ahg2, total_mass_ah_g2, masses_density2, total_mass_density2, total_mass2, mass_topdown2, gc2 = calculate_cell(cell_v)

print("-----------------##--------------------##-------------------##--------------")
print("Cf: {}, Cf2: {}".format(Cf, Cf2))
print("mLi: {}, mLi2: {}".format(mass_ahg["mLi"], mass_ahg2["mLi"]))
print("Density act cat: {}, density act cat 2: {}.".format(mass_ahg["density_active_cat"], mass_ahg2["density_active_cat"]))
print("Total mass: {}, total mass2: {}".format(total_mass, total_mass2))

print(0)
######################################################################
#
#
#
############################## Plot 1 mehrere Celltypes ######################################################
# get figures
fig, axs = plt.subplots(1,2)
legend_entries_cat_active = []
for idx, cell in enumerate(cells):

    #################################################################
    gc = geometric_calculation(cell)
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
    #################################################################

    ################# Plot 1 ##########################################
    axs[0].plot([cell["name"]], total_mass_ah_g["total_mass"], markersize=7, marker="*", label="weight ah/g")
    axs[0].plot([cell["name"]], total_mass_density["total_mass"], markersize=7, marker="+", label="weight density")
    #################################################################

    ################# Plot 2 cathode active materials ###############
    legend_entries_cat_active = plot_elements(axs[1], cell, mass_ahg, "*", postfix="_ah/g", legend_entries=legend_entries_cat_active)
    legend_entries_cat_active = plot_elements(axs[1], cell, masses_density, "+", postfix="_density", legend_entries=legend_entries_cat_active)
    #################################################################


axs[0].legend()
axs[1].legend()

axs[0].set_xlabel("Cell", fontsize="12")
axs[0].set_ylabel("weight in g", fontsize="12")
axs[0].set_title("Total Weight")

axs[1].set_xlabel("Cell", fontsize="12")
axs[1].set_ylabel("weight in g", fontsize="12")
axs[1].set_title("Weight Cathode Active Material")

fig.autofmt_xdate(rotation=30)
##########################################################################################################




############################## Plot2 1 Zelltyp, Variationen ###############################################
cell = cells[1]
variation_labels = ["anode_overhang", "factor_more_capacity_cathode", "cat_porosity", "an_porosity", "sep"]
variations = {
    "anode_overhang": list(np.linspace(0.05, 0.3, 20)),
    "factor_more_capacity_cathode": list(np.linspace(1, 2, 20)),
    "cat_porosity": list(np.linspace(0.1, 0.3, 20)),
    "an_porosity": list(np.linspace(0.1, 0.3, 20)),
    "sep": list(np.linspace(10 * 10**-6, 20 * 10**-6, 20)),

}

############### Single Variations ####################################
fig, axs = plt.subplots(1, len(variation_labels))
fig.suptitle("Single Variations: " + cell["name"])
for e_ax, vl in enumerate(variation_labels):
    var = variations[vl]

    v_total_mass_density=[]
    v_total_mass_ah_g=[]
    v_co_density = []
    v_li_density = []
    v_co_ah_g = []
    v_li_ah_g = []
    v_density_active_cat=[]
    for v in var:
        cell_v = copy.copy(cell)
        cell_v[vl] = v
        inactive_masses, mass_ahg, total_mass_ah_g, masses_density, total_mass_density, total_mass, mass_topdown, gc = calculate_cell(cell_v)
        v_total_mass_density.append(total_mass_density["total_mass"])
        v_total_mass_ah_g.append(total_mass_ah_g["total_mass"])
        v_co_density.append(masses_density["mCo"])
        v_co_ah_g.append(mass_ahg["mCo"])
        v_li_density.append(masses_density["mLi"])
        v_li_ah_g.append(mass_ahg["mLi"])
        v_density_active_cat.append(mass_ahg["density_active_cat"])

    axs[e_ax].plot(var,v_total_mass_ah_g, "-*", label="total mass ah/g", color="blue")
    axs[e_ax].plot(var,v_total_mass_density, "-+", label="total mass density", color="blue")
    axs[e_ax].plot(var,v_co_ah_g, "--*", label="cobalt mass ah/g", color="red")
    axs[e_ax].plot(var,v_co_density, "--+", label="cobalt mass density", color="red")
    axs[e_ax].plot(var,v_li_ah_g, "--*", label="Li mass ah/g", color="orange")
    axs[e_ax].plot(var,v_li_density, "--+", label="Li mass density", color="orange")
    axs[e_ax].plot(var,v_density_active_cat, "--+", label="density active cat", color="black")

    axs[e_ax].set_title("Influence of "+vl)
    axs[e_ax].legend()
    axs[e_ax].set_xlabel(vl+" in %/100")
    axs[e_ax].set_ylabel("weight in g", fontsize="12")

for ax in axs:
    y_upper_lim = max(max(v_total_mass_ah_g), max(v_total_mass_density)) * 1.2
    ax.set_ylim([0, y_upper_lim])


############# Multi Variations #######################################
multi_variation_labels = ["active_thickness","collector_thickness", "porosities"]
multi_variation_xlabels ={
    "active_thickness":"h thickness in m",
    "collector_thickness": "h thickness in m",
    "porosities":"porosities in %"
}
multi_variation_xaxis = {
    "active_thickness": "h",
    "collector_thickness": "h",
    "porosities": "cat_porosity"
}

multi_variations = {
    "active_thickness":{
        "cat": list(np.linspace(30*10**-6, 90*10**-6, 20)),
        "an": list(np.linspace(40*10**-6, 90*10**-6, 20)),
        "sep": list(np.linspace(5*10**-6, 20*10**-6, 20))
    },
    "collector_thickness":{
        "cu": list(np.linspace(5*10**-6, 30*10**-6, 20)),
        "al": list(np.linspace(5*10**-6, 30*10**-6, 20))
    },
    "porosities": {
        "cat_porosity": list(np.linspace(0, 0.5, 20)),
        "an_porosity": list(np.linspace(0, 0.5, 20)),
    }
}

fig, axs = plt.subplots(1, max(2, len(multi_variation_labels)))
fig.suptitle("Multi Variations: " +cell["name"])
for e_ax, vl in enumerate(multi_variation_labels):
    var = multi_variations[vl]

    v_total_mass_density=[]
    v_total_mass_ah_g=[]
    v_co_density = []
    v_li_density = []
    v_co_ah_g = []
    v_li_ah_g = []
    v_hs=[]
    for i in range(0,20):
        cell_v = copy.copy(cell)
        for k,v in var.items():
            cell_v[k] = v[i]


        inactive_masses, mass_ahg, total_mass_ah_g, masses_density, total_mass_density, total_mass, mass_topdown, gc = calculate_cell(cell_v)
        cell_v["h"] = gc["h"]

        v_hs.append(cell_v[multi_variation_xaxis[vl]])
        v_total_mass_density.append(total_mass_density["total_mass"])
        v_total_mass_ah_g.append(total_mass_ah_g["total_mass"])
        v_co_density.append(masses_density["mCo"])
        v_co_ah_g.append(mass_ahg["mCo"])
        v_li_density.append(masses_density["mLi"])
        v_li_ah_g.append(mass_ahg["mLi"])

    axs[e_ax].plot(v_hs,v_total_mass_ah_g, "-*", label="total mass ah/g", color="blue")
    axs[e_ax].plot(v_hs,v_total_mass_density, "-+", label="total mass density", color="blue")
    axs[e_ax].plot(v_hs,v_co_ah_g, "--*", label="cobalt mass ah/g", color="red")
    axs[e_ax].plot(v_hs,v_co_density, "--+", label="cobalt mass density", color="red")
    axs[e_ax].plot(v_hs,v_li_ah_g, "--*", label="Li mass ah/g", color="orange")
    axs[e_ax].plot(v_hs,v_li_density, "--+", label="Li mass density", color="orange")

    axs[e_ax].set_title("Influence of "+vl)
    axs[e_ax].legend()
    axs[e_ax].set_xlabel(multi_variation_xlabels[vl])
    axs[e_ax].set_ylabel("weight in g", fontsize="12")

for ax in axs:
    y_upper_lim = max(max(v_total_mass_ah_g), max(v_total_mass_density)) * 1.2
    ax.set_ylim([0, y_upper_lim])
###########################################################################################################
plt.show()
