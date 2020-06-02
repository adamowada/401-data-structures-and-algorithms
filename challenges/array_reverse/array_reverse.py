def reverseArray(list):
	answer = []
	for i in range(len(list)-1, -1, -1):
		answer.append(list[i])
	return answer