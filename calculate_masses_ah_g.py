from util import calculate_mass_percent_chemistry, cathode_capacity_per_gram, anode_capacity_per_gram, cathode_active_densities, anode_active_densities
from util import DENSITY_CONDUCTIVE_CARBON, DENSITY_PVDF_BINDER

def calculate_masses_ah_g(cell, geometry_calculations):
    # Cathode Active Material
    # calculate the mass of the cat-material via the Ah/g-relationship:
    if "specific_capacity_paper" in cell:
        cap_per_gram = cell["specific_capacity_paper"]
    else:
        cap_per_gram = cathode_capacity_per_gram[cell["cat-chem"]]

    # factor_more_capacity_cathode = 1
    factor_more_capacity_cathode = cell["factor_more_capacity_cathode"]

    mass_active_cat_material = cell["capacity"]*factor_more_capacity_cathode / cap_per_gram

    # Get the shares of the cathode tape mixture am/binder/C --> 90%/5%/5%
    # mass_active_cat_material = mass_cat_material * cell["tape_am_binder_carbon_ratio"]["activematerial"]
    mass_cat_material = mass_active_cat_material / cell["cat_activematerial"]
    # Get the shares of the single objects
    shares = calculate_mass_percent_chemistry(cell["cat-chem"])
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
    vol_cat = geometry_calculations["volume_cathode"]
    cat_porosity = cell["cat_porosity"]
    vol_cat_without_porosity = (1-cat_porosity)*vol_cat
    vol_active_cat_without_porosity = vol_cat_without_porosity * ( (cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]]) / (cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]]+ cell["cat_binder"] / DENSITY_PVDF_BINDER + cell["cat_conductivecarbon"] / DENSITY_CONDUCTIVE_CARBON))
    # vol_inactive=0.2
    # vol_cat_am_without_porosity = (1-cat_porosity)*(1-vol_inactive)*vol_cat

    density_active_cat = mass_active_cat_material/(vol_active_cat_without_porosity*1000000) # g/cm^3
    density_solid_cat = mass_cat_material/(vol_cat_without_porosity*1000000) # g/cm^3
    density_total_cat = mass_cat_material/(vol_cat*1000000)

    print("Calculated density of the total cathode: {density_cat:.2f} g/cm³".format(density_cat=density_total_cat))
    print("Calculated density of the solid cathode: {density_solid_cat:.2f} g/cm³".format(density_solid_cat=density_solid_cat))
    print("Calculated density of the cathode active material: {dens_cat:.2f} g/cm³".format(dens_cat=density_active_cat))
    print("vol cat: {vol_cat:.2f} cm³, vol cat w/o porosity: {vol_cat_without_porosity:.2f} cm³, vol active cat w/o porosity: {vol_active_cat_without_porosity:.2f} cm³".format( vol_cat=vol_cat*1000000,vol_cat_without_porosity=vol_cat_without_porosity*1000000, vol_active_cat_without_porosity=vol_active_cat_without_porosity*1000000))


    # Anode Active Material
    # calculate the mass of the anode
    cap_per_gram = anode_capacity_per_gram[cell["an-chem"]]
    mass_active_an_material = (cell["capacity"] * factor_more_capacity_cathode) / cap_per_gram
    mass_an_material = mass_active_an_material / cell["an_activematerial"]
    print("Anode material total: {mantotal:.2f} g. Mass anode active material: {manacttotal:.2f} g".format(mantotal=mass_an_material, manacttotal=mass_active_an_material))

    # calculate the density of the anode
    va = geometry_calculations["volume_anode"]
    an_porosity=cell["an_porosity"]
    density_active_an = mass_an_material/((1-an_porosity) * va*1000000) # g/cm^3
    density_total_anode = mass_an_material/(va*1000000)
    print("Calculated density of the total anode: {dens_tan:.2f} g/cm³".format(dens_tan=density_total_anode))
    print("Calculated density of the anode active material: {dens_an:.2f} g/cm³".format(dens_an=density_active_an))


    return {"mass_cat_material": mass_cat_material,
            "mass_active_cat_material": mass_active_cat_material,
            "density_active_cat": density_active_cat,
            "density_solid_cat": density_solid_cat,
            "mass_an_material": mass_an_material,
            "mass_active_an_material": mass_active_an_material,
            "density_active_an": density_active_an,
            "mLi": mLi,
            "mNi": mNi,
            "mMn": mMn,
            "mCo": mCo,
            "mAl": mAl,
            "mFe": mFe,
            "mP": mP,
            "shares": shares
            }