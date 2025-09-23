# REPLACE thermal conductivity correction
thermal_conductivity = base_tc * (1 - 0.0015 * (transmutation["Re"] + transmutation["Os"]))
