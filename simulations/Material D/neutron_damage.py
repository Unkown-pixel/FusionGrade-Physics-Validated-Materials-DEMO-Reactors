# REPLACE helium_concentration calculation for V-alloys
helium_concentration = 10 * dpa  # 10 appm/dpa for V-alloys (J. Nucl. Mater. 558, 2022)

# ADD V-specific transmutation
def get_transmutation(composition, dpa):
    return {"Cr": 0.083 * dpa, "Mn": 0.021 * dpa}  # FISPACT-II coefficients for V-base
