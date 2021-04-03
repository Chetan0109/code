import unittest
import pandas as pd
import teradata

host,username,password = '#######','######', '#######'

def hello_world():
	return 'hello world'
	
def load_excel():
	df = pd.read_excel('customer.xls',header=0, separator = '|')
	
	df2 = pd.DataFrame(df['|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active'].str.split('|').tolist())
	df2.columns = ['chetan','H', 'Customer_Name', 'ID','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name','State','Country','DOB','Is_Active']
	df2 = df2.drop(['chetan','H'], axis = 1)
	
	#Formatting date columns
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

			
def Load_Final_Data():
	print("Hi")
	udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
	with udaExec.connect(method="odbc",system=host, username=username,password=password, driver="Teradata") as connect:
		df = pd.read_sql("select distinct country from dev_wrk.customers_tmp",connect)
		df.columns = ['country']

		for i in range(len(df)):
			COUNTRY_CODE = str(df["country"].loc[i])

			cursor = connect.cursor()
			select_query = "select distinct country from dev_wrk.countries where country_code = '" + COUNTRY_CODE + "'" 

			cursor.execute(select_query)
			# get all records
			records = cursor.fetchall()
			for row in records:
				str1 = row[0]
				#Check Main table presence and fetch the tablename
				table = checkTablePresence(str1)
				#inserting the data into final tables based on country
				insert_query = "INSERT INTO DEV_WRK." + table + "SEL * FROM DEV_WRK.CUSTOMERS_TMP WHERE COUNTRY = '"+ COUNTRY_CODE + "'"
				cursor.execute(insert_query)
			#print("Total number of rows in table: ", cursor.rowcount)
	return "pass"
	
def checkTablePresence(str1):
	table_name = 'TABLE_' + str1
	udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
	with udaExec.connect(method="odbc",system=host, username=username,password=password, driver="Teradata") as connect:
		cursor = connect.cursor()
		sel_query = "select count(*) from dbc.tables where tablename = '" + table_name + "' and databasename = 'DEV_WRK'"
		create_query = "CREATE SET TABLE DEV_WRK." + table_name +",FALLBACK ,NO BEFORE JOURNAL,NO AFTER "+"JOURNAL,CHECKSUM = DEFAULT,DEFAULT MERGEBLOCKRATIO(CUSTOMER_NAME VARCHAR(255) CHARACTER SET LATIN NOT"+" CASESPECIFIC NOT NULL,CUSTOMER_ID VARCHAR(18) CHARACTER SET LATIN NOT CASESPECIFIC NOT "+"NULL,CUSTOMER_OPEN_DATE DATE FORMAT 'YYYY/MM/DD' NOT NULL,LAST_CONSULTED_DATE DATE FORMAT "+"'YYYY/MM/DD',VACCINATION_TYPE CHAR(5) CHARACTER SET LATIN NOT CASESPECIFIC,Doctor_Consulted CHAR(255)"+" CHARACTER SET LATIN NOT CASESPECIFIC,State CHAR(5) CHARACTER SET LATIN NOT CASESPECIFIC,Country"+" CHAR(5) CHARACTER SET LATIN NOT CASESPECIFIC,Post_Code INTEGER,DATE_OF_BIRTH DATE FORMAT 'MM/DD/YYYY',"+"ACTIVE_CUSTOMER CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC)PRIMARY INDEX ( CUSTOMER_ID,CUSTOMER_NAME );"

		cursor.execute(sel_query)
		# get all records
		records = cursor.fetchall()
		for row in records:
			
			if(row[0] == 0):
				print("table not present")
				#creating the required table
				cursor.execute(create_query)
	return table_name
				
	


class MyFirstTests(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello_world(),'hello world')
		
	def test_data(self):
		self.assertEqual(load_excel(),5)
		
	def test_table(self):
		self.assertEqual(Load_Final_Data(),'pass')


		
	

if __name__ == '__main__':
    unittest.main()
