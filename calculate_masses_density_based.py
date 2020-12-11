from util import anode_densities, cathode_densities, cathode_active_densities, calculate_mass_percent_chemistry, anode_active_densities
from util import DENSITY_CONDUCTIVE_CARBON, DENSITY_PVDF_BINDER

def calculate_masses_density_based(cell, geometry_calculations):

    # Cathode
    vol_cat = geometry_calculations["volume_cathode"]
    cat_active_density = cathode_active_densities[cell["cat-chem"]]
    shares = calculate_mass_percent_chemistry(cell["cat-chem"])

    cat_porosity = cell["cat_porosity"]
    vol_cat_without_porosity = (1 - cat_porosity) * vol_cat
    vol_active_cat_without_porosity = vol_cat_without_porosity * (
                (cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]]) / (
                    cell["cat_activematerial"] / cathode_active_densities[cell["cat-chem"]] +
                    cell["cat_binder"] / DENSITY_PVDF_BINDER + cell["cat_conductivecarbon"] / DENSITY_CONDUCTIVE_CARBON))

    mass_active_cat_material = 1000000 * vol_active_cat_without_porosity * cat_active_density
    mass_cat_material = mass_active_cat_material / cell["cat_activematerial"]

    # mass_active_cat_material = mass_cat_material
    mLi = shares["pLi"] * mass_active_cat_material
    mNi = shares["pNi"] * mass_active_cat_material
    mMn = shares["pMn"] * mass_active_cat_material
    mCo = shares["pCo"] * mass_active_cat_material
    mAl = shares["pAl"] * mass_active_cat_material
    mFe = shares["pFe"] * mass_active_cat_material
    mP = shares["pP"] * mass_active_cat_material

    # Anode
    an_porosity = cell["an_porosity"]
    an_active_density = anode_active_densities[cell["an-chem"]]

    vol_an = geometry_calculations["volume_anode"]
    vol_an_without_porosity = (1 - an_porosity) * vol_an
    vol_active_an_without_porosity = vol_an_without_porosity * (
                (cell["an_activematerial"] / anode_active_densities[cell["an-chem"]]) / (
                    cell["an_activematerial"] / anode_active_densities[cell["an-chem"]] +
                    cell["an_binder"] / DENSITY_PVDF_BINDER + cell["an_conductivecarbon"] / DENSITY_CONDUCTIVE_CARBON))


    mass_active_an_material = 1000000*vol_active_an_without_porosity*an_active_density
    mass_an_material = mass_active_an_material / cell["an_activematerial"]

    # mass_an_material = 1000000*vol_an*an_density


    print("* Mass calculation of active materials density-based:")
    print("Given: density active cathode: {cat_density:.2f} g/cm³, density anode: {an_density:.2f} g/cm³.".format(cat_density=cat_active_density, an_density=an_active_density))
    print("Calc: density total cathode: {cat_density:.2f} g/cm³, density anode: {an_density:.2f} g/cm³.".format(cat_density=mass_cat_material/(1000000*vol_cat), an_density=mass_an_material/(1000000*vol_an)))
    print("Cathode material total: {mtotal:.2f} g. active cat material: {macm:.2f} g, Li: {mli:.2f} g, Ni: {mni:.2f} g, Mn: {mmn:.2f} g, Co: {mco:.2f} g, Al: {mal:.2f} g, Fe: {mfe:.2f} g, P: {mp:.2f} g".format(mtotal=mass_cat_material, macm=mass_active_cat_material, mli=mLi, mni=mNi, mmn=mMn, mco=mCo, mal = mAl, mfe=mFe, mp=mP))

    print("Anode material total: {mantotal:.2f} g. Mass anode active material: {manacttotal:.2f} g".format(mantotal=mass_an_material, manacttotal=mass_active_an_material))


    return {"mass_cat_material": mass_cat_material,
            "mass_active_cat_material": mass_active_cat_material,
            "mass_an_material": mass_an_material,
            "mass_active_an_material": mass_active_an_material,
            "mLi": mLi,
            "mNi": mNi,
            "mMn": mMn,
            "mCo": mCo,
            "mAl": mAl,
            "mFe": mFe,
            "mP": mP,
            "shares": shares
            }
