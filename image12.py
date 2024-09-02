def solution(query):
	history = ["blank"]
	idx = 0
	
	answer = []
	
	for q in query:
		if "MOV" in q:
			a, url = q.split()
			if url in history:
				idx = history.index(url) 
			else:
				history = history[:idx+1] 
				history.append(url)
				idx += 1
				
		if "DEL" in q:
			a, url = q.split()
			if url not in history or history[idx] == url:
				continue
			else:
				if history.index(url) < idx:
					idx -= 1
				history.remove(url)

		if "BCK" in q:
			if idx != 0:
				idx -= 1
			answer.append(history[idx])
		
		if "FWD" in q:
			if idx < len(history) - 1:
				idx += 1
			answer.append(history[idx])
	
	return answer