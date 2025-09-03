def calc_jump(score, mul):
	mod = (score - 10) // 2
	cm30 = 0.3048
	base_high = 3
	res = []

	if score:
		# LONG JUMP
		# FT.
		long_movement_ft = score * mul
		long_standing_ft = long_movement_ft / 2

		# MT.
		long_movement_mt = round(long_movement_ft * cm30, 1)
		long_standing_mt = round(long_standing_ft * cm30, 1)

		# Apply 0 limit
		long_movement_ft = max(long_movement_ft, 0)
		long_standing_ft = max(long_standing_ft, 0)
		long_movement_mt = max(long_movement_mt, 0)
		long_standing_mt = max(long_standing_mt, 0)

		long_jump = {
			'long_standing_ft': long_standing_ft,
			'long_movement_ft': long_movement_ft,
			'long_standing_mt': long_standing_mt,
			'long_movement_mt': long_movement_mt
		}
		res.append(long_jump)

		# HIGH JUMP
		# FT.
		high_movement_ft = (base_high + mod) * mul
		high_standing_ft = high_movement_ft / 2

		# MT.
		high_movement_mt = round(high_movement_ft * cm30, 1)
		high_standing_mt = round(high_standing_ft * cm30, 1)

		# Apply 0 limit
		high_movement_ft = max(high_movement_ft, 0)
		high_standing_ft = max(high_standing_ft, 0)
		high_movement_mt = max(high_movement_mt, 0)
		high_standing_mt = max(high_standing_mt, 0)

		high_jump = {
			'high_standing_ft': high_standing_ft,
			'high_movement_ft': high_movement_ft,
			'high_standing_mt': high_standing_mt,
			'high_movement_mt': high_movement_mt
		}
		res.append(high_jump)

	return res