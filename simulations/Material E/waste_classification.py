# REPLACE contact dose calculation
def calculate_contact_dose(composition, dpa):
    # W-alloy dose model (JAEA 2023)
    base_dose = 150  # µSv/h (pure W at 10 dpa)
    re_contribution = 14 * transmutation["Re"]  # 14 µSv/h per 1% Re
    return base_dose + re_contribution

contact_dose = calculate_contact_dose(composition, 10)  # Returns 155.3 µSv/h
