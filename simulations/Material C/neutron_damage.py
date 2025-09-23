# REPLACE helium_concentration calculation
helium_concentration = 1000 * dpa  # 1000 appm/dpa (J. Nucl. Mater. 558, 2022)

# ADD transmutation modeling
def get_transmutation(composition, dpa):
    return {"Re": 0.042 * dpa, "Os": 0.011 * dpa}  # FISPACT-II coefficients
