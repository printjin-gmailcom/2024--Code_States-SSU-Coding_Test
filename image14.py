def solution(rounds):
	result = 0
	
	player = ["a", "b", "c", "d"]
	player_idx = {"a":0, "b":1, "c":2, "d":3}
	
	last_couple = ["-"]*4
	for rd in rounds:
		cur_couple = ["-"]*4
		for idx, partner in enumerate(rd):
			if partner == player[idx]:
				result += 1
			elif partner == last_couple[idx]:
				result += 1
			elif rd[player_idx[partner]] == player[idx]:
				cur_couple[idx] = partner

		last_couple = couple[:]
	
	return result