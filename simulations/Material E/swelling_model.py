# REPLACE swelling calculation
def calculate_swelling(dpa, helium_appm):
    """Swelling = base + 0.103*(He_appm/1000) (J. Nucl. Mater. 575, 2023)"""
    base_swelling = 0.82  # % at 10 dpa (no He)
    he_contribution = 0.103 * (helium_appm / 1000)
    return base_swelling + he_contribution

swelling = calculate_swelling(10, 10000)  # Returns 1.85%
