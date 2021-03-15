from pwn import *

def hanoi_pile(disks):
	#number of moves in tower of hanoi given as (2**[num of disks])-1
	count = len(disks)
	moves = (2**count)-1
	return moves

def count_inversions(data):
	#inversions in an array given as number of elements occurring later in the array which are smaller for each element
	inv = 0
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			if(data[i] > data[j]):
				inv += 1
	return inv
	
def main():
	r = remote('45.134.3.200',9660)
	r.recvline()
	r.recvline()
	level = 1
	stage = 1
	while(True):
		data = str(r.recvline(keepends=False))
		if("level 2" in data):
			level = 2
			stage = 1
			continue
		elif("you won" in data):
			print(data)
			break
		#format list
		data = data[data.find('[')+1:]
		data = data[:data.find(']')]
		data = data.split(", ")
		
		if(level == 1):
			#print(data)
			print("Sending Level:",level,"Stage:",stage)
			r.send(str(hanoi_pile(data)))
			stage+=1
		elif(level == 2):
			#print(data)
			for i in range(0,len(data)):
				data[i] = int(data[i])
			print("Sending Level:",level,"Stage:",stage)
			r.send(str(count_inversions(data)))
			stage += 1
main()
		



