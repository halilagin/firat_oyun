import argparse

#  parser.add_argument('--topic-name', default="test" )
#  parser.add_argument('--data', default="test" )
#  args = parser.parse_args()

def test_01():
	f=open("./ornek001.txt", "r") #r-> read w->write
	content=f.read()
	f.close()
	print (content)
	

def test_02():
	f=open("yazi.txt", "w")
	f.write("bugun carsamba, test\n")
	f.close()

def test_03():
	f=open("./ornek003.txt", "r") #r-> read w->write
	lines=f.readlines()
	f.close()

	for line in lines:
		line=line[:-1] #string in son karakterini siler, son karakter new line \n
		if line=="carsamba":
			print("CARSAMBA")
		else:
			print ("'"+line+"'")





if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--run', default="test_01" )
	parser.add_argument('--test', default="12" )
	args = parser.parse_args()


	if args.run=="test_01":
		test_01()
	elif args.run=="test_02":
		test_02()
	elif args.run=="test_03":
		test_03()
	

