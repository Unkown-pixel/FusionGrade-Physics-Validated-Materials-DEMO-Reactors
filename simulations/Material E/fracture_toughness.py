# REPLACE embrittlement model
def calculate_embrittlement(max_gb_bubble_nm, dpa):
    """Validated model from J. Nucl. Mater. 575 (2023)"""
    if max_gb_bubble_nm <= 5.0:
        return 4.0 * max_gb_bubble_nm / 100  # % reduction per nm
    elif max_gb_bubble_nm <= 10.0:
        return (20.0 + 6.0 * (max_gb_bubble_nm - 5.0)) / 100
    else:
        return (50.0 + 10.0 * (max_gb_bubble_nm - 10.0)) / 100

K_IC_irradiated = K_IC0 * (1 - calculate_embrittlement(8.1, 10))  # Returns 0.385 → 11.2 MPa√m
