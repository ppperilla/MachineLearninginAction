
if __name__ == '__main__':
	dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	number = len(dataset[0])-1

	# print ("dataset[0] = %s"%(dataset[0]))
	for i in range(number):
		print("i = %d \n"%(i))
		featlist = [example[i] for example in dataset]
		print ("featlist = %s\n"%(featlist))
		unique_vals =  set(featlist)
		print ("unique_vals = %s\n"%(unique_vals))
