# REPLACE embrittlement model for V-alloys
def calculate_embrittlement(max_gb_bubble_nm, dpa):
    if max_gb_bubble_nm <= 5.0:  # V-alloys tolerate smaller bubbles
        return 3.5 * max_gb_bubble_nm * (1 + 0.05 * max(0, dpa - 5)) / 100
    else:
        return 8.0 * (max_gb_bubble_nm - 5) / 100 + calculate_embrittlement(5.0, dpa)
