def solution(n, accounts, transfer):
	answer = []
	
	account_table = {} 
	for customer, account in accoutns:
		account_table[account] = customer
	
	transfer_table = {str(i):0 for i in range(1, 1 + n)} 	
	
	for from_, to_, money in transfers:
		fr_cus = account_table[from_]
		to_cus = account_table[to_]
		
		if fr_cus == to_cus:
			continue
		
		transfer_table[fr_cus] += int(money)
	
	for i in range(1, 1+n):
		answer.append(transfer_table[str(i)])
	
	return answer