def get_jump(score):
	mod = (score - 10) // 2
	cm = 0.3048
	base_high = 3
	res = []

	if score:
		# Long jump
		# Ft.
		long_movement_ft = score * 1
		long_standing_ft = long_movement_ft // 2

		# Mt.
		long_movement_mt = round(long_movement_ft * cm)
		long_standing_mt = round(long_standing_ft * cm)

		# Apply 0 limit
		long_movement_ft = max(long_movement_ft, 1)
		long_standing_ft = max(long_standing_ft, 1)
		long_movement_mt = max(long_movement_mt, 1)
		long_standing_mt = max(long_standing_mt, 1)

		long_jump = {
			'long_standing_ft': long_standing_ft,
			'long_movement_ft': long_movement_ft,
			'long_standing_mt': long_standing_mt,
			'long_movement_mt': long_movement_mt
		}
		res.append(long_jump)

		# High jump
		# Ft.
		high_movement_ft = base_high + mod
		high_standing_ft = high_movement_ft // 2

		# Mt.
		high_movement_mt = round(high_movement_ft * cm)
		high_standing_mt = round(high_standing_ft * cm)

		# Apply 0 limit
		high_movement_ft = max(high_movement_ft, 1)
		high_standing_ft = max(high_standing_ft, 1)
		high_movement_mt = max(high_movement_mt, 1)
		high_standing_mt = max(high_standing_mt, 1)

		high_jump = {
			'high_standing_ft': high_standing_ft,
			'high_movement_ft': high_movement_ft,
			'high_standing_mt': high_standing_mt,
			'high_movement_mt': high_movement_mt
		}
		res.append(high_jump)

	return res