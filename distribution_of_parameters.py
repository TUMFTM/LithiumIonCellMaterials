from cells import *
import matplotlib.pyplot as plt
import pandas as pd

'''
Plotting file to show the distributions of parameters of the cells
'''

anode_overhang = [cell["anode_overhang"] for cell in all_cells]
design = [cell["design"] if "design" in cell else None for cell in all_cells]
type = [cell["type"] if "type" in cell else None for cell in all_cells]
case_to_stack_layer_factor = [cell["case_to_stack_layer_factor"] if "case_to_stack_layer_factor" in cell else None for cell in all_cells ]
porosity_Separator = [cell["porosity_Separator"] if "porosity_Separator" in cell else None for cell in all_cells ]
cat_porosity = [cell["cat_porosity"] if "cat_porosity" in cell else None for cell in all_cells ]
an_porosity = [cell["an_porosity"] if "an_porosity" in cell else None for cell in all_cells ]
ease_packaging_factor = [cell["ease_packaging_factor"] if "ease_packaging_factor" in cell else None for cell in all_cells ]
an = [cell["an"] if "an" in cell else None for cell in all_cells ]
cat = [cell["cat"] if "cat" in cell else None for cell in all_cells ]
sep = [cell["sep"] if "sep" in cell else None for cell in all_cells ]
al = [cell["al"] if "al" in cell else None for cell in all_cells ]
cu = [cell["cu"] if "cu" in cell else None for cell in all_cells ]

df_params = pd.DataFrame({
    "anode_overhang": anode_overhang,
    "design": design,
    "type": type,
    "porosity_Separator": porosity_Separator,
    "cat_porosity": cat_porosity,
    "an_porosity": an_porosity,
    "ease_packaging_factor": ease_packaging_factor,
    "case_to_stack_layer_factor": case_to_stack_layer_factor,
    "an": an,
    "sep": sep,
    "al": al,
    "cu": cu,
    "cat": cat
})

print(df_params.describe())
print(df_params.min())
print(df_params.max())

# df_params.plot.kde(bw_method=2)
# df_params.groupby(["design"]).boxplot()
# df_params["an"].groupby(["type"]).boxplot()

######################### Schichtdicken ########################################################
# Schichtidcken zu Mikrometer
df_params[["an", "cat", "sep", "cu", "al"]] = df_params[["an", "cat", "sep", "cu", "al"]].apply(lambda x: x*1000000)

axs = df_params[["an", "cat", "sep", "cu", "al"]].boxplot(rot=30)
axs.set_ylabel("thickness in μm", fontsize=14)
axs.set_title("Thickness stack parts", fontsize=14)
axs.tick_params(axis='x', labelsize=14)
axs.tick_params(axis='y', labelsize=14)
plt.savefig("plots/distribution_of_parameters/boxplot_layer.png")

axs = df_params[["an", "cat", "sep", "cu", "al", "design"]].groupby(["design"]).boxplot(rot=30, figsize=(15,15))
[ax.set_ylabel("thickness in μm", fontsize=14) for ax in axs]
[ax.tick_params(axis='x', labelsize=14) for ax in axs]
[ax.tick_params(axis='y', labelsize=14) for ax in axs]
plt.savefig("plots/distribution_of_parameters/boxplot_layer_by_design.png")



axs = df_params[["an", "cat", "sep", "cu", "al", "type"]].groupby(["type"]).boxplot(rot=30, figsize=(15,15))
[ax.set_ylabel("thickness in μm", fontsize=14) for ax in axs]
[ax.tick_params(axis='x', labelsize=14) for ax in axs]
[ax.tick_params(axis='y', labelsize=14) for ax in axs]
plt.savefig("plots/distribution_of_parameters/boxplot_layer_by_type.png")

######################### Andere Parameter ########################################################
df_params  = df_params.drop(["an", "cu", "sep", "al", "cat"], axis=1)
# df_params.plot.kde(bw_method=2)

f, axs = plt.subplots(nrows=1,ncols=1, figsize=(9,9))
axs = df_params.boxplot(ax=axs, rot=13, figsize=(15,15))
axs.set_ylabel("value parameters", fontsize=14)
axs.tick_params(axis='x', labelsize=14)
axs.tick_params(axis='y', labelsize=14)
axs.set_xticklabels(["anode overhang", "porosity sep", "porosity cat", "porosity an", "ease packaging factor", "case to stack layer factor"])
plt.savefig("plots/distribution_of_parameters/boxplot_params.png")

axs = df_params.groupby(["design"]).boxplot(rot=13, figsize=(15,15))
[ax.set_ylabel("value parameters", fontsize=14) for ax in axs]
[ax.tick_params(axis='x', labelsize=14) for ax in axs]
[ax.tick_params(axis='y', labelsize=14) for ax in axs]
[ax.set_xticklabels(["anode overhang", "porosity sep", "porosity cat", "porosity an", "ease packaging factor", "case to stack layer factor"]) for ax in axs]
plt.savefig("plots/distribution_of_parameters/boxplot_params_by_design.png")

axs = df_params.groupby(["type"]).boxplot(rot=13, figsize=(15,15))
[ax.set_ylabel("value parameters", fontsize=14) for ax in axs]
[ax.tick_params(axis='x', labelsize=14) for ax in axs]
[ax.tick_params(axis='y', labelsize=14) for ax in axs]
[ax.set_xticklabels(["anode overhang", "porosity sep", "porosity cat", "porosity an", "ease packaging factor", "case to stack layer factor"]) for ax in axs]
plt.savefig("plots/distribution_of_parameters/boxplot_params_by_type.png")

# plt.figure()
# df_params.boxplot(rot=10)
plt.show()