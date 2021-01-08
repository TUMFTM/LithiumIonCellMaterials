# Estimate Resources in Li-Ionen Cells


## Abstract
How many resources are in a li-ion cell? Depending on the geometry, capacity, chemistry, etc. 
this model estimates the number of materials in g.

## How to use
1. You will need [python3](https://www.python.org/) and virtual environments on your machine.
1. Create a virtual environment in this folder. `virtualenv env -p python3` and activate `source env\bin\activate`
1. Install the requirements listed in requirements.txt: `pip install -r requirements.txt`
1. According to cell type, open main_prismatic.py, or main_cylindric.py. Choose from the built-in cells as indicated in the file. Save file.
1. Run `python main_prismatic.py` or `python main_cylindric.py`
1. The script outputs material shares and weights for different methods. 

## Description of scripts
cells.py\
Contains the cell raw data from the literature. A total of 17 cells, cylindric to prismatic are ready-to-use.

main_prismatic.py / main_cylindric.py\
Use these files to calculate the masses and shares for one specific cell.

main_plotter.py\
plots several cells next to each other. contains some sensitivity measures

sensitivity_density_based.py\
Contains the sensitivity analysis for the density-based approach

## Methods
![Setup](/images/blocks.png)

### Capacity-based method

The capacity-based method makes use of the specific capacity in Ah/g of the active materials and the rated capacity of the cell in Ah to calculate the mass of the active materials. The specific capacities for active materials can be found in the literature. Unfortunately, one always runs into uncertainties, since the specific capacities are given with a certain bandwidth. Neicoorperation, for example, gives the value of ≥ 190 mAh/g in their datasheet for NCA electrodes [8]. Other sources from scientific papers either give ranges scraped from the literature or exact numbers for one exemplarily reverse-engineered cell as [Lain2019].

Further uncertainties come from the factor_more_capacity_cathode factor. As mentioned above, this captures the nature of built-in cathode capacities are always larger than the cell’s rated capacity. To smooth out this factor, one can look at the densities of the electrode w/o porosity and compare this value with the ones from the literature. Necessary here ist the tape formula, thus the ratio between active material, binder, and CC. Backtracking through the model, we can calculate a value for the factor, which allows for an exact match between the model-estimated densities and the ones from literature.

### Density-based method

This method directly uses the densities of the active materials and the geometric properties i.e. the volume of the electrodes to calculate the mass of the active electrode parts. The model brings us to the aim of knowing the mass percentages of the active materials much quicker, as there is no need for adapting parameters. This model is in a way integrated also in the capacity-based method to allow for backtracking and correcting the factor_more_capacity_cathode.

## Article and Description of Datasets
[Smart Mobility Blog - How many resources are in a lithium-ion cell](https://smarte-mobilitaet-blog.ftm.mw.tum.de/index.php/2020/04/02/how-many-resources-are-inside-of-a-lithium-ion-cell/)

[Same Article on Researchgate](https://www.researchgate.net/publication/340870640_Resources_in_a_lithium-ion_cell)
#### Contact
lukas.merkle@tum.de\
[FTM Website](https://www.mw.tum.de/ftm/lehrstuhl/mitarbeiter/smarte-mobilitaet/lukas-merkle-m-sc/)
