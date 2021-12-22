import mysql.connector

class Crud ():
    
    def __init__(self,):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="restflask"
        )

        self.cursor  = self.connection.cursor()
    
    def create(self, sql, data):
        self.cursor.execute(sql, data)
        self.connection.commit()

        result = self.cursor.lastrowid

        self.cursor.close()
        self.connection.close()

        return (result)

    def read(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        
        self.cursor.close()
        self.connection.close()
        
        return (result)
    
    def updateOrDelete(self, sql, data):
        self.cursor.execute(sql, data)
        self.connection.commit()
        
        lines = self.cursor.rowcount

        self.cursor.close()
        self.connection.close()
        
        return(lines)
