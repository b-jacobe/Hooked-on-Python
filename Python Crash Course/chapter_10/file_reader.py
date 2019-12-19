"""
file_reader.py

Reading the contents of a text
file.

Created: 3-26-19
@author: Brian Jacobe

"""
def num_after_point(x):
	s = str(x)
	if not '.' in s:
		return 0
	return len(s) - s.index('.') - 1


filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(num_after_point(pi_string))
