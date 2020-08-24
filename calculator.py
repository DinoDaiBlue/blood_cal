def interface():
	print("My Program")
	while True:
		print("Options")
		print("1 - HDL")
		print("9 - Quit")
		choice = input("Enter your choice: ")
		if choice == '9':
			return
		elif choice == '1':
			HDL_driver()

def HDL_driver():
	HDL_num = get_HDL_input()
	# Get input
	message = check_HDL_value(HDL_num)
	# Check
	output_the_message(HDL_num, message)	 
	return 
	# Out put
def get_HDL_input():
	HDL_num = input("Please input the HDL value")
	HDL_num = int(HDL_num)
	return HDL_num
def check_HDL_value(HDL_num):
	if HDL_num >= 60:
		return "Normal"
	elif 40 <= HDL_num < 60:
		return "Borderline Low"
	else:
		return "Low"
def output_the_message(test_result, analysis):
	print("The value is {}".format(test_result))
	print("It is" + analysis)
interface()

