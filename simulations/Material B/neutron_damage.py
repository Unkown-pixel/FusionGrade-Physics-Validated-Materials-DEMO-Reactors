# REPLACE helium_concentration calculation
helium_concentration = 1000 * dpa  # 1000 appm/dpa for W-alloys (J. Nucl. Mater. 575, 2023)

# ADD transmutation modeling
def get_transmutation(composition, dpa):
    return {
        "Re": 0.038 * dpa,  # W→Re
        "Os": 0.010 * dpa,  # Re→Os
        "Cr": 0.019 * dpa   # V→Cr
    }
