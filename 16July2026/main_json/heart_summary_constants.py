heart_inner_keys = [
    "totalPlaqueVolume",
    "lowDensityNonCalcifiedPlaqueVolume",
    "totalNonCalcifiedPlaqueVolume",
    "totalCalcifiedPlaqueVolume"
]

# define coordinate for getting the required data for each heading (x1, y1, x2, y2)
heart_summary_headings = {
    'Right Coronary Artery (RCA)': (0, 0, 1, 0.45),
    'Right Posterior Descending Artery (R-PDA)': (0, 0.4, 0.5, 1),
    'Right Posterior Lateral Branch (R-PLB)': (0.5, 0.4, 1, 1),
    'Left Main and Left Anterior Descending (LM+LAD)': (0, 0, 1, 0.45),
    'First Diagonal Branch (D1)': (0, 0.4, 0.5, 1),
    'Second Diagonal Branch (D2)': (0.5, 0.4, 1, 1),
    'Circumflex (Cx)': (0, 0, 1, 0.45),
    'First Obtuse Marginal (OM1)': (0, 0.4, 0.5, 1),
    'Second Obtuse Marginal (OM2)': (0.5, 0.4, 1, 1),
    'Left Posterior Descending Artery (L-PDA)': (0, 0, 0.5, 0.45),
    'Left Posterior Lateral Branch (L-PLB)': (0.5, 0, 1, 0.45),
    'Ramus Intermedius (RI)': (0, 0.42, 1, 1)
}


def get_dict_template(info):
    return {
        "info": info,
        "normalVariant": False,
        **{k: {"mm3": None, "pav": None} for k in heart_inner_keys}
    }


def heart_summary_json():
    return {
        #
        "rightCoronaryArtery": get_dict_template("Right Coronary Artery (RCA)"),
        "rightPosteriorDescendingArtery": get_dict_template("Right Posterior Descending Artery (R-PDA)"),
        "rightPosteriorLateralBranch": get_dict_template("Right Posterior Lateral Branch (R-PLB)"),
        #
        "leftMainAndLeftAnteriorDescending": get_dict_template("Left Main and Left Anterior Descending (LM+LAD)"),
        "firstDiagonalBranch": get_dict_template("First Diagonal Branch (D1)"),
        "secondDiagonalBranch": get_dict_template("Second Diagonal Branch (D2)"),
        #
        "circumflex": get_dict_template("Circumflex (Cx)"),
        "firstObtuseMarginal": get_dict_template("First Obtuse Marginal (OM1)"),
        "secondObtuseMarginal": get_dict_template("Second Obtuse Marginal (OM2)"),
        #
        "leftPosteriorDescendingArtery": get_dict_template("Left Posterior Descending Artery (L-PDA)"),
        "leftPosteriorLateralBranch": get_dict_template("Left Posterior Lateral Branch (L-PLB)"),
        "ramusIntermedius": get_dict_template("Ramus Intermedius (RI)"),
    }