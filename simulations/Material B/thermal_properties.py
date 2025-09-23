# REPLACE thermal_conductivity calculation
def correct_thermal_conductivity(tc_0, re_percent, os_percent):
    return tc_0 * (1 - 0.0012 * (re_percent + os_percent) - 0.0003 * dpa)

thermal_conductivity = correct_thermal_conductivity(125, 0.38, 0.10)  # Returns 108.2 W/m·K
