# REPLACE dose calculation
def calculate_dose_after(decay_years, composition):
    # V-4Cr-4Ti activation model (JAEA 2023)
    base_dose = 18  # µSv/h at 1m (1 day post-shutdown)
    return base_dose * (0.5 ** (decay_years / 12.4))  # Cr-51 half-life = 12.4 days
