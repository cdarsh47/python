import pymysql.cursors

def main():
	connection = pymysql.connect(host="localhost",user="root",password='',database='test',cursorclass=pymysql.cursors.DictCursor)

	db_object = connection.cursor()

	return db_object,connection

if __name__=='__main__':
	main()