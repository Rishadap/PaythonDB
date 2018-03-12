import cx_Oracle
import sqlite3
import pyodbc
import re
#dbtype = raw_input("Please Provide the type of database:")
#sql_query= raw_input("Please Provide the sql query eg:- database type has to be appened with the table name DEPT@ORACLE:").replace(,"@oracle", "").lower()
sql_query= raw_input("Please Provide the sql query eg:- database type has to be appened with the table name DEPT@ORACLE:")
sql_query=re.sub(r"\b(?<!')(\w+)(?!')\b", lambda match: match.group(1).lower(), sql_query)
print sql_query
if '@oracle' in sql_query:
	conn_string= raw_input("Please Provide the Oracle database connection string eg:- user/password@hostname or IP Adress/database name:")
	conn_orcl = cx_Oracle.connect(conn_string)
	tables=re.findall(r"\w+@ORACLE", sql_query,re.IGNORECASE)
	#print table1
	print sql_query
	for t in tables:
		cur_orcl = conn_orcl.cursor()
		#print(dbtype)
		print(conn_string)
		#t=t.lower()
		#print t
		#a=t.lower()
		#print a
		u=str.replace(t,"@oracle", "")
		print u 
		#print u
		cur_orcl.execute('select * from ' + u)	
		#cur_sqlite_rows=cur_orcl.fetchall()
		#print cur_sqlite_rows
		#print cur_sqlite_rows	
		print u
		str3 =''
		str4 =''
		for i in cur_orcl.description: 
			str4 = str4+ '?,'		
			#print len(i)
			#print cur_orcl.description		
			str1 = str(i[1]).strip("<type 'cx_Oracle.'>")
			str2= str(i[0])+' '+ str1+'('+str((i[2]))+'),'
			str3 +=str2
			#str4 = str4 + i
			print str3
			conn_sqlite = sqlite3.connect('sqlite_db')
			cur_sqlite=conn_sqlite.cursor()
		#print str4
		print str4.rstrip(",")	
		cur_sqlite.execute('DROP TABLE IF EXISTS ' + u.upper())
		print 'CREATE TABLE '+u.upper()+ ' (' +str3.rstrip(",") +')'
		cur_sqlite.execute('CREATE TABLE '+u.upper()+ ' (' +str3.rstrip(",") +')')	
		conn_sqlite.commit()			
	#print len(str3.rstrip(",").replace(" ","").split())
	#print list(str3.rstrip(","))
		#print str2
		#print str3
		#for result in cur_orcl:
		cur_sqlite_rows=cur_orcl.fetchall()
		print cur_sqlite_rows
	#print cur_sqlite.sqlite3_column_count() 
	#print len(cur_sqlite_rows)
		#print cur_sqlite_rows
		#count=''
		#for i in cur_sqlite_rows:
		#+str(cur_sqlite_rows)+
			#print 'INSERT INTO '+ u.upper()+ '(' + str4.rstrip(",") +') VALUES('+str(i).replace(",)",")").replace("(","(")+')'
			#cur_sqlite.execute('INSERT INTO '+ u.upper()+ '(' + str4.rstrip(",") +') VALUES('+str(i).replace(",)",")").replace("(","(")+')')
			#cur_sqlite.execute('INSERT INTO '+ u.upper()+ 'VALUES ('+cur_sqlite_rows +')')
		#cur_sqlite.executemany('INSERT INTO '+ u.upper()+ ' VALUES ('+str(cur_sqlite_rows) +')')
		#cur.executemany('INSERT INTO' + u.upper()+ 'VALUES (?)', cur_sqlite_rows)
	#print str3.rstrip(",")	
	#print len(set(cur_sqlite_rows))
	#print cur_sqlite_rows
		cur_sqlite.executemany( 'INSERT INTO ' + u.upper()+ ' VALUES ('+str4.rstrip(",")+') ',cur_sqlite_rows)	
		#COM = 'INSERT INTO '+ u.upper()+ ' (Short_Model) ' + ' VALUES ('+ '(%s)'
		#print COM
		#cur_sqlite.executemany(COM,cur_sqlite_rows)
		#cur_sqlite.execute( 'INSERT INTO '+ u.upper()+ '(' + str4.rstrip(",") +') VALUES('+str(cur_sqlite_rows)+')' )	
		# list should ne converted to rows
		#for results in a:	
		#print a[1]
		#for result in cur_orcl:
		#print result
		#print str4.rstrip(",")
		#cur_sqlite.execute('''INSERT INTO DEPT (DEPT_NO,DEPT_NAME,DEPT_LOCATION) VALUES (?,?,?)''',(result[0],result[1],result[2]))
		#conn_sqlite.commit()
		print sql_query.replace(r"@oracle","",re.IGNORECASE)
		conn_sqlite.commit()
	#a=sql_query.replace(r"@oracle","",re.IGNORECASE)
	#print a 
	#cur_sqlite.execute(a)
if '@sqlserver' in sql_query:
	conn_string= raw_input("Please Provide the sqlserver database connection string eg:- Driver={SQL Server}; Server=LAPTOP-U7V56UQE\SQLEXPRESS;uid=;pwd=;Trusted_Connection=yes:")
	conn_sqlserver=pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-U7V56UQE\SQLEXPRESS;uid=;pwd=;Trusted_Connection=yes")
	#conn_orcl = cx_Oracle.connect(conn_string)
	tables=re.findall(r"\w+@SQLSERVER", sql_query,re.IGNORECASE)
	#print table1
	print sql_query
	for t in tables:
		cur_sqlserver = conn_sqlserver.cursor()		
		print(conn_string)
		u=str.replace(t,"@sqlserver", "")
		print u 	
		cur_sqlserver.execute('select * from ' + u)				
		print u
		str3 =''
		str4 =''
		for i in cur_sqlserver.description: 
			str4 = str4+ '?,'		
			str1 = str(i[1]).strip("<type>").replace("'","")
			str2= str(i[0])+' '+ str1+'('+str((i[3]))+'),'
			str3 +=str2
			#str4 = str4 + i
			print str3
			conn_sqlite = sqlite3.connect('sqlite_db')
			cur_sqlite=conn_sqlite.cursor()
		print str4.rstrip(",")	
		cur_sqlite.execute('DROP TABLE IF EXISTS ' + u.upper())
		print 'CREATE TABLE '+u.upper()+ ' (' +str3.rstrip(",") +')'
		cur_sqlite.execute('CREATE TABLE '+u.upper()+ ' (' +str3.rstrip(",") +')')	
		conn_sqlite.commit()			
		cur_sqlite_rows=cur_sqlserver.fetchall()
		print cur_sqlite_rows
		cur_sqlite.executemany( 'INSERT INTO ' + u.upper()+ ' VALUES ('+str4.rstrip(",")+') ',cur_sqlite_rows)	
		print sql_query.replace(r"@oracle","",re.IGNORECASE).replace(r"@sqlserver","",re.IGNORECASE)
		cur_sqlite.execute(sql_query.replace(r"@oracle","",re.IGNORECASE).replace(r"@sqlserver","",re.IGNORECASE))
		cur_sqlite_rows=cur_sqlite.fetchall()	
		conn_sqlite.commit()
		print cur_sqlite_rows	
		#cur_sqlite_rows()				
	cur_orcl.close()
	cur_sqlserver.close()