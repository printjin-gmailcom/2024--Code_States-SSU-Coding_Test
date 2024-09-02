def solution(n, snow):
  available = [2*i+1 for i in range(n)] 
  
  answer = []
  
  overflow = 0
  for av, s in zip(available, snow):
	  total_snow = s + overflow 
	  if av - total_snow >= 0: 
		  answer.append(total_snow)
		  overflow = 0
		else: 
			answer.append(av)
			overflow = total_snow - av
	
	return answer