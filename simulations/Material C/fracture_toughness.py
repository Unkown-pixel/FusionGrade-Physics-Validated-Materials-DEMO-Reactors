# REPLACE embrittlement model
def calculate_embrittlement(max_gb_bubble_nm, dpa):
  return 5.0 * max_gb_bubble_nm * (1 + 0.1 * max(0, dpa - 5)) / 100  # % reduction
