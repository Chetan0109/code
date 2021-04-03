import unittest
import pandas as pd
import teradata
#from mycode import *




def hello_world():
	return 'hello world'
	
def load_excel():
	df = pd.read_excel('customer.xls',header=0, separator = '|')
	
	df2 = pd.DataFrame(df['|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active'].str.split('|').tolist())
	df2.columns = ['chetan','H', 'Customer_Name', 'ID','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name','State','Country','DOB','Is_Active']
	df2 = df2.drop(['chetan','H'], axis = 1)
	#print(df2)
	df2['Open_Date'] = df2['Open_Date'].str[0:4] + "/" + df2['Open_Date'].str[4:6] + "/" + df2['Open_Date'].str[6:8]
	df2['Last_Consulted_Date'] = df2['Last_Consulted_Date'].str[0:4] + "/" + df2['Last_Consulted_Date'].str[4:6] + "/" + df2['Last_Consulted_Date'].str[6:8]
	df2['DOB'] = df2['DOB'].str[0:2] + "/" + df2['DOB'].str[2:4] + "/" + df2['DOB'].str[4:8]
	print(df2)
	index = df2.index
	number_of_rows = len(index)
	insertIntoTable(df2)
	return number_of_rows
	
def insertIntoTable(df2):
	print('entered here')
	udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
	host,username,password = '#######','######', '#######'
	with udaExec.connect(method="odbc",system=host, username=username,password=password, driver="Teradata") as connect:
		print('entered')
		df3=pd.read_sql("select count(*) from dev_wrk.customers_tmp",connect)
		print(df3)
		connect.execute("delete from dev_wrk.customers_tmp")
		df3=pd.read_sql("select count(*) from dev_wrk.customers_tmp",connect)
		print(df3)

		try:
			for i in range(len(df2)):
				connect.execute("INSERT INTO DEV_WRK.CUSTOMERS_TMP VALUES(" + "'" + str(df2["Customer_Name"].loc[i]) + "','"+ str(df2["ID"].loc[i]) + "','" + str(df2["Open_Date"].loc[i]) + "','" + str(df2["Last_Consulted_Date"].loc[i]) + "','" + str(df2["Vaccination_Id"].loc[i]) + "','" + str(df2["Dr_Name"].loc[i]) + "','" + str(df2["State"].loc[i]) + "','" + str(df2["Country"].loc[i]) + "',0,'"+ str(df2["DOB"].loc[i]) + "','"+ str(df2["Is_Active"].loc[i]) + "')")
				
			return 'pass'
		except Exception as e:
			print(e)
			#pass
		#finally:
			#return number_of_rows


class MyFirstTests(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello_world(),'hello world')
		
	def test_data(self):
		self.assertEqual(load_excel(),5)
		
	#def test_table(self):
		#self.assertEqual(insertIntoTable(),'pass')


		
	

if __name__ == '__main__':
    unittest.main()
