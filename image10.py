def solution(plants, power, demand):
	total_power = 0
	for est, dur, po in plants:
		if est + dur >= 2050:
			total_power += po
	
	needed = demand - total_power 
	if needed < 0:
		answer = 0
	else:
		answer = needed // power
		shortage = needed % power
		if shortage > 0:
			answer += 1
	
	return answer