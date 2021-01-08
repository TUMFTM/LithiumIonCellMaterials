from cells import PHEV2, pouch_fantasy1, pouch_fantasy2, BEV2, EIG_ePLB_C020, Schmalstieg_pris, LG_HB4, eGolf_UF261591
from geometric import geometric_calculation
from calculate_masses_ah_g import calculate_masses_ah_g
from calculate_masses_density_based import calculate_masses_density_based
from calculate_masses_inactive import calculate_masses_inactive, calculate_total_mass
from calculate_masses_top_down import calculate_masses_top_down
from util import theoretical_capacity
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import copy
import random
import time
from SALib.sample import saltelli
from SALib.analyze import sobol, morris
import numpy as np


cell=BEV2

# Choose other cells from cells, e.g.:
# cell = EIG_ePLB_C020
# cell = eGolf_UF261591

an = cell["an"]
cat = cell["cat"]
sep = cell["sep"]
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

    theo_capa = theoretical_capacity(cell, gc)

    return {"inactive_masses": inactive_masses,
            "mass_ahg": mass_ahg,
            "total_mass_ah_g": total_mass_ah_g,
            "masses_density": masses_density,
           "total_mass_density": masses_density,
           "total_mass": total_mass,
           "mass_topdown": mass_topdown,
            "gc": gc,
            "theo_capa": theo_capa}


ANODE_OVERHANG_BASELINE = 1.1
CASE_TO_STACK_LAYER_FACTOR_BASELINE = 0.9
def create_baseline(cell):
    cell["factor_more_capacity_cathode"] = 1
    cell["anode_overhang"] = ANODE_OVERHANG_BASELINE
    cell["case_to_stack_layer_factor"] = CASE_TO_STACK_LAYER_FACTOR_BASELINE
    cell["an"] = an * 1
    cell["cat"] = cat * 1
    cell["sep"] = sep * 1
    return cell


if __name__ == "__main__":

    # Create Plots
    fig, axs = plt.subplots(2,3, sharey="row", figsize=(10,7))


    # Vary anode_overhang
    cell = create_baseline(cell)

    mass_densities = []
    anode_overhang = []
    theo_capas = []
    for ao in list(np.linspace(1, 1.25, 20)):
        cell["anode_overhang"] = ao
        anode_overhang.append(ao)
        mass_densities.append(calculate_cell(cell)["masses_density"])
        theo_capas.append(calculate_cell(cell)["theo_capa"])

    axs[0][0].plot(anode_overhang, [md["mass_cat_material"] for md in mass_densities], label="mass_cat_material", color="blue")
    axs[0][0].plot(anode_overhang, [md["mass_an_material"] for md in mass_densities], label="mass_an_material", color="red")
    axs[0][0].axvline(x=ANODE_OVERHANG_BASELINE, ymin=0, ymax=1, label="Baseline", color="black")
    # axs[0].plot(anode_overhang, [md["C_theo_cat_Ah"] for md in theo_capas], label="C_theo_cat_Ah")
    axs[0][0].legend()
    axs[0][0].set_xlabel("anode overhang in %/100")
    axs[0][0].set_ylabel("active electrode mass in g")

    # put axes
    for i in range(0,2):
        for j in range(0,3):
            axs[i][j].grid()




    # Vary case_to_stack_layer_factor
    cell = create_baseline(cell)
    mass_densities = []
    case_to_stack_layer_factors = []
    for f in list(np.linspace(0.8, 1, 20)):
        cell["case_to_stack_layer_factor"] = f
        # cell["anode_overhang"] = 1.15
        case_to_stack_layer_factors.append(f)
        mass_densities.append(calculate_cell(cell)["masses_density"])

    axs[0][1].plot(case_to_stack_layer_factors, [md["mass_cat_material"] for md in mass_densities], label="mass_cat_material", color="blue")
    axs[0][1].plot(case_to_stack_layer_factors, [md["mass_an_material"] for md in mass_densities], label="mass_an_material", color="red")
    axs[0][1].axvline(x=CASE_TO_STACK_LAYER_FACTOR_BASELINE, ymin=0, ymax=1, label="Baseline", color="black")
    axs[0][1].legend()
    axs[0][1].set_xlabel("case_to_stack_layer_factor in %/100")



    # Vary anode thickness
    cell = create_baseline(cell)
    anode_thickness_0 = cell["an"]
    mass_densities = []
    anode_thickness_multiplicators = []
    anode_thickness = []
    for f in list(np.linspace(0.5, 2, 20)):
        cell["an"] = anode_thickness_0 * f
        anode_thickness_multiplicators.append(f)
        anode_thickness.append(anode_thickness_0*f)
        mass_densities.append(calculate_cell(cell)["masses_density"])

    axs[0][2].plot(anode_thickness, [md["mass_cat_material"] for md in mass_densities],
                label="mass_cat_material", color="blue")
    axs[0][2].plot(anode_thickness, [md["mass_an_material"] for md in mass_densities],
                label="mass_an_material", color="red")
    axs[0][2].axvline(x=anode_thickness_0, ymin=0, ymax=1, label="Baseline", color="black", linestyle="--")
    axs[0][2].legend()
    axs[0][2].set_xlabel("anode thickness in m")



    # Vary cathode thickness
    cell = create_baseline(cell)
    cathode_thickness_0 = cell["cat"]
    mass_densities = []
    cathode_thickness_multiplicators = []
    cathode_thickness = []
    for f in list(np.linspace(0.5, 2, 20)):
        cell["cat"] = cathode_thickness_0 * f
        cathode_thickness_multiplicators.append(f)
        cathode_thickness.append(cathode_thickness_0 * f)
        mass_densities.append(calculate_cell(cell)["masses_density"])

    axs[1][0].plot(cathode_thickness, [md["mass_cat_material"] for md in mass_densities],
                label="mass_cat_material", color="blue")
    axs[1][0].plot(cathode_thickness, [md["mass_an_material"] for md in mass_densities],
                label="mass_an_material", color="red")
    axs[1][0].axvline(x=cathode_thickness_0, ymin=0, ymax=1, label="Baseline", color="black")
    axs[1][0].legend()
    axs[1][0].set_xlabel("cathode thickness in m")
    axs[1][0].set_ylabel("active electrode mass in g")


    # Vary anode and cathode thickness
    cell = create_baseline(cell)
    cathode_thickness_0 = cell["cat"]
    mass_densities = []
    cathode_thickness_multiplicators = []
    cathode_thickness = []
    anode_thickness_0 = cell["an"]
    anode_thickness_multiplicators = []
    anode_thickness = []
    for f in list(np.linspace(0.5, 2, 50)):
        cell["cat"] = cathode_thickness_0 * f
        cathode_thickness_multiplicators.append(f)
        cathode_thickness.append(cathode_thickness_0 * f)
        cell["an"] = anode_thickness_0 * f
        anode_thickness_multiplicators.append(f)
        anode_thickness.append(anode_thickness_0 * f)
        mass_densities.append(calculate_cell(cell)["masses_density"])

    axs[1][1].plot(cathode_thickness_multiplicators, [md["mass_cat_material"] for md in mass_densities],
                label="mass_cat_material", color="blue")
    axs[1][1].plot(cathode_thickness_multiplicators, [md["mass_an_material"] for md in mass_densities],
                label="mass_an_material", color="red")
    axs[1][1].axvline(x=1, ymin=0, ymax=1, label="Baseline_cat", color="black")
    axs[1][1].axvline(x=1, ymin=0, ymax=1, label="Baseline_an", color="black")
    axs[1][1].legend()
    axs[1][1].set_xlabel("factor thickness in %/100")



    # Vary separator thickness
    cell = create_baseline(cell)
    sep_thickness_0 = cell["sep"]
    mass_densities = []
    sep_thickness_multiplicators = []
    sep_thickness = []

    for f in list(np.linspace(0.5, 2, 50)):
        cell["sep"] = sep_thickness_0 * f
        sep_thickness_multiplicators.append(f)
        sep_thickness.append(sep_thickness_0 * f)
        mass_densities.append(calculate_cell(cell)["masses_density"])

    axs[1][2].plot([s*1000 for s in sep_thickness], [md["mass_cat_material"] for md in mass_densities],
                label="mass_cat_material", color="blue")
    axs[1][2].plot([s*1000 for s in sep_thickness], [md["mass_an_material"] for md in mass_densities],
                label="mass_an_material", color="red")
    axs[1][2].axvline(x=sep_thickness_0*1000, ymin=0, ymax=1, label="Baseline_sep", color="black")
    axs[1][2].legend()
    axs[1][2].set_xlabel("sep_thickness in mm")
    plt.savefig("plots/sensitivity_density_based/singlevar_influence.png")




    ########### MIN / MAX Szenarios #################################
    cell = create_baseline(cell)
    cell_min = copy.deepcopy(cell)
    cell_max = copy.deepcopy(cell)
    cell_mean = copy.deepcopy(cell)
    cell_cont = copy.deepcopy(cell)

    masses_density_real = calculate_cell(cell)["masses_density"]

    # Min Szenario
    cell_min["anode_overhang"] = 1.15
    cell_min["case_to_stack_layer_factor"] = 0.8
    cell_min["an"] = 36*10**-6
    cell_min["cat"] = 38*10**-6
    cell_min["sep"] = 24.7*10**-6
    cell_min["ease_packaging_factor"] = 1.15

    masses_density_min = calculate_cell(cell_min)["masses_density"]

    # Mean Szenario
    cell_mean["anode_overhang"] = 1.1
    cell_mean["case_to_stack_layer_factor"] = 0.845
    cell_mean["an"] = cell_mean["an"] * 1
    cell_mean["cat"] = cell_mean["cat"] * 1
    cell_mean["sep"] = cell_mean["sep"] * 1

    masses_density_mean = calculate_cell(cell_mean)["masses_density"]

    # Max Szenario
    cell_max["anode_overhang"] = 1.011
    cell_max["case_to_stack_layer_factor"] = 0.86
    cell_max["an"] = 86*10**-6
    cell_max["cat"] = 81*10**-6
    cell_max["sep"] = 7*10**-6
    cell_max["ease_packaging_factor"] = 1

    masses_density_max = calculate_cell(cell_max)["masses_density"]

    fig, axs = plt.subplots(1, 2, sharey="row")

    axs[0].plot(0, [masses_density_min["mass_an_material"]], color="red", marker="+", markersize=10)
    axs[0].plot(0, [masses_density_min["mass_cat_material"]], color="blue", marker="+", markersize=10)
    axs[0].plot(27, [masses_density_real["mass_cat_material"]], color="blue", marker=".")
    axs[0].plot(27, [masses_density_real["mass_an_material"]], color="red", marker=".")
    axs[0].plot(49, [masses_density_max["mass_an_material"]], color="red", marker="*", markersize=10)
    axs[0].plot(49, [masses_density_max["mass_cat_material"]], color="blue", marker="*", markersize=10)
    axs[0].set_xlabel("Evolving Scenario. +: Min, *: Max", fontsize=14)
    axs[0].set_ylabel("active electrode mass in g", fontsize=14)
    axs[0].tick_params(axis='x', labelsize=14)
    axs[0].tick_params(axis='y', labelsize=14)

    # Continuous spectrum
    n = 50
    c_ao = np.linspace(cell_min["anode_overhang"], cell_max["anode_overhang"], n)
    c_ctlf = np.linspace(cell_min["case_to_stack_layer_factor"], cell_max["case_to_stack_layer_factor"], n)
    c_an = np.linspace(cell_min["an"], cell_max["an"], n)
    c_cat = np.linspace(cell_min["cat"], cell_max["cat"], n)
    c_sep = np.linspace(cell_min["sep"], cell_max["sep"], n)
    c_epf = np.linspace(cell_min["ease_packaging_factor"], cell_max["ease_packaging_factor"], n)

    # Continuous spectrum
    mass_densities_cont = []
    nn = []
    for f in range(0, n):
        cell_cont["anode_overhang"]=c_ao[f]
        cell_cont["case_to_stack_layer_factor"]=c_ctlf[f]
        cell_cont["an"]=c_an[f]
        cell_cont["cat"]=c_cat[f]
        cell_cont["sep"]=c_sep[f]
        cell_cont["ease_packaging_factor"]=c_epf[f]
        nn.append(f)
        mass_densities_cont.append(calculate_cell(cell_cont)["masses_density"])

    axs[0].plot(nn,  [md["mass_cat_material"] for md in mass_densities_cont], color="blue")
    axs[0].plot(nn,  [md["mass_an_material"] for md in mass_densities_cont], color="red")
    # tikzplotlib.save("test.tex")
    axs[0].grid()



    # Monte Carlo spectrum
    mass_densities_mc=[]
    nn_mc=[]
    axs[1].set_xlabel("Monte Carlo szenarios", fontsize=14)
    axs[1].set_ylabel("active electrode mass in g", fontsize=14)
    axs[1].tick_params(axis='x', labelsize=14)
    axs[1].tick_params(axis='y', labelsize=14)
    random.seed(time.time())

    for i in range(0,500):

        rand0 = random.randint(0,49)
        rand1 = random.randint(0,49)
        rand2 = random.randint(0,49)
        rand3 = random.randint(0,49)
        rand4 = random.randint(0,49)

        cell_cont["anode_overhang"] = c_ao[rand0]
        cell_cont["case_to_stack_layer_factor"] = c_ctlf[rand1]
        cell_cont["an"] = c_an[rand2]
        cell_cont["cat"] = c_cat[rand3]
        cell_cont["sep"] = c_sep[rand4]
        nn_mc.append(i)
        mass_densities_mc.append(calculate_cell(cell_cont)["masses_density"])

    axs[1].plot(nn_mc, [md["mass_cat_material"] for md in mass_densities_mc], color="blue", marker=".", linestyle="")
    axs[1].plot(nn_mc, [md["mass_an_material"] for md in mass_densities_mc], color="red", marker=".", linestyle="")
    # tikzplotlib.save("test.tex")
    axs[1].grid()
    plt.savefig("plots/sensitivity_density_based/corridor_montecarlo.png")


    ######################## USING SALib ##############################################
    evaluate = "mass_an_material"

    def evaluate_model(cell, X):
        cell["anode_overhang"] = X[0]
        cell["case_to_stack_layer_factor"] = X[1]
        cell["ease_packaging_factor"] = X[2]
        cell["an"] = X[3]
        cell["cat"] = X[4]
        cell["sep"] = X[5]
        cell["an_porosity"] = X[6]
        cell["cat_porosity"] = X[7]


        return calculate_cell(cell)["masses_density"][evaluate]

    problem = {
        'num_vars': 8,
        'names': ['anode_overhang', 'case_to_stack_layer_factor',"ease_packaging_factor", 'an', "cat", "sep", "an_porosity", "cat_porosity"],
        'bounds': [
            [cell_max["anode_overhang"], cell_min["anode_overhang"]],
            [cell_min["case_to_stack_layer_factor"], cell_max["case_to_stack_layer_factor"]],
            [cell_max["ease_packaging_factor"], cell_min["ease_packaging_factor"]],
            [cell_min["an"], cell_max["an"]],
            [cell_min["cat"], cell_max["cat"]],
            [cell_max["sep"], cell_min["sep"]],
            [0.09, 0.296],
            [0.2, 0.38]]
    }

    # # https://stackoverflow.com/questions/45280278/could-salib-support-other-probability-distribution-when-inputing-parameters-in-s/51763834
    param_values = saltelli.sample(problem, 1000)
    # param_values[:, 0] = sp.stats.norm.ppf(param_values[:, 0], 0, np.pi / 2.)
    # param_values[:, 1] = sp.stats.norm.ppf(param_values[:, 1], 0, np.pi / 2.)
    # param_values[:, 2] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)
    # param_values[:, 3] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)
    # param_values[:, 4] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)
    # param_values[:, 5] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)
    # param_values[:, 6] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)
    # param_values[:, 7] = sp.stats.norm.ppf(param_values[:, 2], 0, np.pi / 2.)

    Y = np.zeros([param_values.shape[0]])
    for i, X in enumerate(param_values):
        Y[i] = evaluate_model(cell, X)

    Si = sobol.analyze(problem, Y, print_to_console=True)

    f, axs = plt.subplots(nrows=1, ncols=1, figsize=(13,7))
    axs.plot(problem["names"], Si["S1"], marker="+", markersize=14, linestyle="", label="1. order")
    axs.plot(problem["names"], Si["ST"], marker="+", markersize=14, linestyle="", label="Total order")
    axs.set_xlabel("Sobol sensitivivty method", fontsize=14)
    axs.set_ylabel("share model variance", fontsize=14)
    axs.tick_params(axis='x', labelsize=14, labelrotation=10)
    axs.tick_params(axis='y', labelsize=14)
    axs.set_ylim([0, 0.7])
    axs.set_title("Model output: "+ evaluate, fontsize=14)
    axs.legend(prop={'size': 14})
    plt.savefig("plots/sensitivity_density_based/sobol_s1_st_{}.png".format(evaluate))

    # print(cell_min["an"], cell_max["an"])
    plt.show()




