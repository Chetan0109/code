import unittest
import pandas as pd

#from mycode import *

def hello_world():
	return 'hello world'
	
def load_excel():
	df = pd.read_excel('customer.xls',header=0)
	print(df)
	index = df.index
	number_of_rows = len(index)
	return number_of_rows

class MyFirstTests(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello_world(),'hello world')
		
	def test_data(self):
		self.assertEqual(load_excel(),5)


		
	

if __name__ == '__main__':
    unittest.main()