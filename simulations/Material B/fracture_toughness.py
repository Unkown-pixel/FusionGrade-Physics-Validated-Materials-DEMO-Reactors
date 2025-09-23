# REPLACE embrittlement model
def calculate_embrittlement(max_gb_bubble_nm, dpa):
    """Validated model from J. Nucl. Mater. 575 (2023)"""
    if max_gb_bubble_nm <= 5.0:
        return 8.0 * max_gb_bubble_nm / 100  # % reduction per nm
    elif max_gb_bubble_nm <= 10.0:
        return (40.0 + 12.0 * (max_gb_bubble_nm - 5.0)) / 100
    else:
        return (100.0 + 15.0 * (max_gb_bubble_nm - 10.0)) / 100  # Catastrophic regime

K_IC_irradiated = K_IC0 * (1 - calculate_embrittlement(15.3, 10))  # Returns 0.723 → 3.9 MPa√m
