arr = [0] * int(input())
ptr = 0

def record(order_id):
	global ptr
	global arr
	arr[ptr] = order_id
	ptr += 1
	if ptr == len(arr):
		ptr = 0

def get_last(i):
	if i <= ptr:
		return arr[ptr-i]
	else:
		return arr[len(arr)-i+ptr]

while True:
	operation = input()
	if operation == '1':
		record(input())
	elif operation == '2':
		print(get_last(int(input())))
	else:
		break