import unittest
import pandas as pd

#from mycode import *

def hello_world():
	return 'hello world'
	
def load_excel():
	df = pd.read_excel('customer.xls',header=0, separator = '|')
	
	df2 = pd.DataFrame(df['|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active'].str.split('|').tolist())
	df2.columns = ['chetan','H', 'Customer_Name', 'Customer_Id','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name','State','Country','DOB','Is_Active']
	df2 = df2.drop(['chetan'], axis = 1)
	print(df2)
	index = df2.index
	number_of_rows = len(index)
	return number_of_rows

class MyFirstTests(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello_world(),'hello world')
		
	def test_data(self):
		self.assertEqual(load_excel(),5)


		
	

if __name__ == '__main__':
    unittest.main()