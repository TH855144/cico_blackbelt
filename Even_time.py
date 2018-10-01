#!/usr/bin/python3
import datetime

def currtime():
	now = datetime.datetime.now()
	print ("Current date and time : ")
	print (now.strftime("%Y-%m-%d %H:%M:%S"))

def evencount(numb):
	string = numb['sequence']
	n = string.count(',')
	string1 = string.split(", ")
	#total1 = len(string1)
	ar = []
	for i in string1:
		if (int(i) % 2) == 0:
			ar.append(i)
	print (len(ar),"numbers are Even out of 100")
	print (ar)
	return	


numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
numb1 = numbers[0]

currtime()
evencount(numb1)

