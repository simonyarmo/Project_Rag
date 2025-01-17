import mysql.connector


def createTableList():
  file = open("SQLData", "w")
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Redcar123!",
    database="DataForAIModel"
  )
  mycursor = mydb.cursor(buffered=True)
  mycursor.execute("SHOW TABLES")
  tables = mycursor.fetchall()
  # Show all tables
  for table in tables:
      table_string =""
      table_name = table[0]
      print(f"Table: {table_name}")
      table_string= "Table: {"+ table_name+"}"

      # Get column names and data types for the table
      mycursor.execute(f"DESCRIBE {table_name}")
      columns = mycursor.fetchall()

      for column in columns:
          column_name = column[0]
          data_type = column[1]
          print(f"  Column: {column_name}, Data Type: {data_type}")
          table_string= table_string+"  Column: {" +column_name+ "}, Data Type: {"+data_type+"}"
      file.write(table_string+"\n")
      print()  # Add a blank line between tables

  mycursor.close()
  mydb.close()


def promptUser():
   userInput = input("Enter a question: " )
   return userInput

if __name__ == "__main__":
  createTableList()
  
   



