def get_minimum(bed, table):
	w1, h1, c1 = bed
	w2, h2, c2 = table
	
	a = (w1+w2)*max(h1, h2)
	b = (h1+h2)*max(w1, w2)
	c = (w1+h2)*max(h1, w2)
	d = (h1+w2)*max(w1, h2)
	
	return min(a, b, c, d)
	
def solution(beds, tables, cost):
	price = float("inf")
	
	for i in range(len(beds)):
		for j in range(len(tables)):
			
			size = get_minimum(beds[i], tables[j])
			case_cost = size * cost + beds[i][2] + tables[j][2]
			
			price = min(case_cost, price)
	
	return price