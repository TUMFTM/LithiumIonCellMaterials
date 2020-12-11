'''
This file contains the geometric calculations for different cell types
Rundzellen
'''
import math

def __calculate_stack_geometry(cell):
    l= cell["l"]
    b= cell["b"]
    h= cell["h"]

    # cellvolume
    cell_volume = l*b*h # m³

    h_stack = cell["sep"]+cell["an"]+cell["cu"]+cell["an"]+cell["sep"]+cell["cat"]+cell["al"]+cell["cat"]

    # N_sheets = int(h / h_stack)
    N_sheets = float(h / h_stack)

    if "case_to_stack_layer_factor" in cell:
        b_sheets = b
        l_sheets = l
        sheet_surface_case = b_sheets * l_sheets  # in m²
        sheet_surface = sheet_surface_case * cell["case_to_stack_layer_factor"]
    else:
        b_sheets = b - 2*cell["housing_thickness"]
        l_sheets = l - 11*10**-3
        sheet_surface = b_sheets * l_sheets # in m²

    surface_anode = sheet_surface* 2 * N_sheets # double coated # in m²
    #surface_cathode = sheet_surface* 2 * N_sheets * (1 - cell["anode_overhang"]) # double coated # in m²
    surface_cathode = (sheet_surface* 2 * N_sheets)/cell["anode_overhang"] # double coated # in m²

    volume_cathode = surface_cathode * cell["cat"] # in m³
    volume_anode = surface_anode * cell["an"] # in m³
    volume_separator = sheet_surface*2*N_sheets * cell["sep"] # in m³

    print(cell["name"])
    print("* Geometric calculations {} cell. Type: Stack".format(cell["type"]))
    print("N sheets: {N}. Sheet surface: {sheet_surface:.2f} cm². Anode surface: {ass:.2f} cm². Cathode surface: {cs:.2f} cm²".format(N=N_sheets, sheet_surface=sheet_surface*10000, ass=surface_anode*10000,cs=surface_cathode*10000))
    print("Anode volume: {anvol:.2f} cm³, cathode volume: {catvol:.2f} cm³, sep volume: {sepvol:.2f} cm³.".format(anvol=volume_anode*1000000, catvol=volume_cathode*1000000, sepvol=volume_separator*1000000))
    return {"h": h_stack,
            "N":N_sheets,
            "surface_cathode": surface_cathode,
            "volume_cathode": volume_cathode,
            "surface_anode": surface_anode,
            "volume_anode": volume_anode,
            "volume_separator": volume_separator,
            "sheet_surface": sheet_surface}

def __calculate_2_wickel_geometry_upright(cell):
    tape_h = cell["sep"] + cell["an"] + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"] + cell["al"] + cell["cat"]
    r = (cell["h"] - (2*cell["housing_thickness"])) / 2
    b_w = ( (cell["b"]- (2*cell["housing_thickness"]))/2 ) - 2*r
    anode_overhang = cell["anode_overhang"]
    D0 = cell["D0"]
    D1 = 2*r

    # Calculate cylindric part
    ease_packaging_factor = cell["ease_packaging_factor"]
    N = (D1 - D0) / (2 * tape_h * ease_packaging_factor)
    L_tape_cylindric = math.pi * N * (D1 + (tape_h*ease_packaging_factor) * (N - 1))
    surface_cylindric_part = L_tape_cylindric * cell["l_jellyroll"]

    # calculate stack part
    L_tape_stack_part = N*b_w
    surface_stack_part = L_tape_stack_part * cell["l_jellyroll"]
    # surface_stack_part=0

    # Total surface of the tape, one sided
    total_surface_wickel = (surface_cylindric_part + surface_stack_part) *2 # times to because 2 wickel

    # From Here on 2 Wickel are considered

    # Anode
    surface_anode = total_surface_wickel*2 # double coated
    volume_anode = surface_anode * cell["an"]

    # Cathode
    surface_cathode = (total_surface_wickel/anode_overhang) * 2  # double coated, anode overhang
    volume_cathode = surface_cathode * cell["cat"]

    # Separator
    volume_separator = total_surface_wickel * cell["sep"] # single sided

    print(cell["name"])
    print("* Geometric calculations {} cell. Type: 2-wickel".format(cell["type"]))
    print("N wickel: {N}. total surface: {total_surface:.2f} cm². Anode surface: {ass:.2f} cm². Cathode surface: {cs:.2f} cm²".format(
            N=N, total_surface=total_surface_wickel * 10000, ass=surface_anode * 10000, cs=surface_cathode * 10000))
    print("Anode volume: {anvol:.2f} cm³, cathode volume: {catvol:.2f} cm³, sep volume: {sepvol:.2f} cm³.".format(
        anvol=volume_anode * 1000000, catvol=volume_cathode * 1000000, sepvol=volume_separator * 1000000))

    return {"tape_h": tape_h,
            "N": N,
            "surface_cathode": surface_cathode,
            "volume_cathode": volume_cathode,
            "surface_anode": surface_anode,
            "volume_anode": volume_anode,
            "volume_separator": volume_separator,
            "total_surface_wickel": total_surface_wickel}

def __calculate_2_wickel_geometry(cell):
    tape_h = cell["sep"] + cell["an"] + cell["cu"] + cell["an"] + cell["sep"] + cell["cat"] + cell["al"] + cell["cat"]
    r = (cell["h"] - (2*cell["housing_thickness"])) / 4 # radius of the cylindric jellyroll part
    l_w = ( (cell["l"]- (2*cell["housing_thickness"]))) - 2*r # stack part length of the jellyroll
    anode_overhang = cell["anode_overhang"]
    D0 = cell["D0"]
    D1 = 2*r

    # Calculate cylindric part
    ease_packaging_factor = cell["ease_packaging_factor"]
    N = (D1 - D0) / (2 * tape_h * ease_packaging_factor)
    L_tape_cylindric = math.pi * N * (D1 + (tape_h*ease_packaging_factor) * (N - 1))
    surface_cylindric_part = L_tape_cylindric * cell["b_jellyroll"]

    # calculate stack part
    L_tape_stack_part = 2*N*l_w
    surface_stack_part = L_tape_stack_part * cell["b_jellyroll"]
    # surface_stack_part=0

    # Total surface of the tape, one sided
    total_sufrace_1_wickel = (surface_cylindric_part + surface_stack_part)
    total_sufrace_2_wickel =  total_sufrace_1_wickel*2 # times to because 2 wickel

    # From Here on 2 Wickel are considered

    # Anode
    surface_anode = (total_sufrace_2_wickel)*2 # double coated
    volume_anode = surface_anode * cell["an"]

    # Cathode
    surface_cathode = (total_sufrace_2_wickel/anode_overhang) * 2  # double coated, anode overhang
    volume_cathode = surface_cathode * cell["cat"]

    # Separator
    volume_separator = total_sufrace_2_wickel * cell["sep"] * 2 # two separators

    print(cell["name"])
    print("* Geometric calculations {} cell. Type: 2-wickel".format(cell["type"]))
    print("N wickel: {N}. total surface: {total_surface:.2f} cm². Anode surface: {ass:.2f} cm². Cathode surface: {cs:.2f} cm²".format(
            N=N, total_surface=total_sufrace_2_wickel * 10000, ass=surface_anode * 10000, cs=surface_cathode * 10000))
    print("Anode volume: {anvol:.2f} cm³, cathode volume: {catvol:.2f} cm³, sep volume: {sepvol:.2f} cm³.".format(
        anvol=volume_anode * 1000000, catvol=volume_cathode * 1000000, sepvol=volume_separator * 1000000))



    return {"tape_h": tape_h,
            "N": N,
            "surface_cathode": surface_cathode,
            "volume_cathode": volume_cathode,
            "surface_anode": surface_anode,
            "volume_anode": volume_anode,
            "volume_separator": volume_separator,
            "total_surface_wickel": total_sufrace_2_wickel}

def geometric_calculation_prismatic(cell):

    gc=None

    if cell["structure"] == "stack":
        gc = __calculate_stack_geometry(cell)

    if cell["structure"] == "2-wickel":
        gc = __calculate_2_wickel_geometry(cell)

    return gc


def geometric_calculation_cylindric(cell):

    # Get the diameters of the cell.
    D0 = cell["D0"] # inner diameter of the roll in m
    D1_inside = cell["D1"] - 2 * cell["housing_thickness"] # outer diameter of roll in m

    # Calculate the total thickness of the tape
    h = cell["sep"]+cell["an"]+cell["cu"]+cell["an"]+cell["sep"]+cell["cat"]+cell["al"]+cell["cat"]
    ease_packaging_factor = cell["ease_packaging_factor"]
    N = (D1_inside - D0) / (2 * h*ease_packaging_factor)
    L_tape = math.pi * N * (D0 + h * (N - 1))

    # surface cathode
    anode_overhang = cell["anode_overhang"]
    # surface_cathode = (1- anode_overhang)* L_tape * cell["l_jellyroll"]*2
    surface_cathode = (L_tape * cell["l_jellyroll"]*2) / anode_overhang

    # volume cathode:
    volume_cathode = surface_cathode*cell["cat"] # m³

    # surface anode
    surface_anode = L_tape * cell["l_jellyroll"]*2

    # volume anode
    volume_anode = surface_anode*cell["an"]

    print(cell["name"])
    print("* Doing the geometric calculations, based on the thickness od the layers.")
    print("Turns: {turns:.2f}, length: {length:.2f} m, surface tape: {st:.3f} m², surface cat: {scat:.3f} m²"
          " volume wickel: {vw:.2f} cm³, volume cat: {vc:.2f} cm³,"
          " volume cell body: {vcb:.2f} cm³, h: {h:.2f} mm".format(turns=N, length=L_tape, st=L_tape * cell["l_jellyroll"],
                                                                   scat=surface_cathode,
                                                                   vw=(L_tape * cell["l_jellyroll"] * h) * 1000000,
                                                                   vc=volume_cathode * 1000000,
                                                                   vcb=(cell["l"]*((cell["D1"]/2)**2)*math.pi)*1000000, h=h*1000))

    # Volume separator
    volume_separator = L_tape*cell["sep"]*2

    return {"D1_inside": D1_inside,
            "h": h,
            "N":N,
            "L_tape":L_tape,
            "surface_cathode": surface_cathode,
            "volume_cathode": volume_cathode,
            "surface_anode": surface_anode,
            "volume_anode": volume_anode,
            "volume_separator": volume_separator}


def geometric_calculation(cell):
    gc = None
    if cell["type"] == "18650" or cell["type"] == "21700":
        gc = geometric_calculation_cylindric(cell)

    if cell["type"] == "prismatic":
        gc = geometric_calculation_prismatic(cell)

    if cell["type"] == "pouch":
        gc= geometric_calculation_prismatic(cell)

    if gc == None:
        raise ValueError
    else:
        return gc