from pathlib import Path
from datetime import datetime
import mysql.connector

class Crud ():
    
    def __init__(self,):
        
        self.connectBdError = 0
        time = datetime.now()
        fileDestination = str(Path('aplication/logs/DbConnect.txt').absolute())

        try:
            
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="restflask"
            )
            
            with open(fileDestination, "a") as arquivo:
                arquivo.write('\n [ {} ] SUCCESS >> CONNECTION SUCCESS !!'.format(time.strftime('%d/%m/%Y %H:%M:%S')))

            self.cursor  = self.connection.cursor()
       
        except Exception as erro:
            self.connectBdError = 1
            
            with open(fileDestination, "a") as arquivo:
                arquivo.write('\n [ {} ] ERRO >> {}'.format(time.strftime('%d/%m/%Y %H:%M:%S'),str(erro)))
            
    
    def create(self, sql, data):
        
        if (self.connectBdError == 0):
            
            self.cursor.execute(sql, data)
            self.connection.commit()

            result = self.cursor.lastrowid

            self.cursor.close()
            self.connection.close()

            return (result)
        
        else:
            return ("Erro")

    def read(self, sql):
        
        if (self.connectBdError == 0):
            
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        
            self.cursor.close()
            self.connection.close()
        
            return (result)
        
        else:
            return ("Erro")
    
    def update(self, sql, data):
        
        if (self.connectBdError == 0):
            
            self.cursor.execute(sql, data)
            self.connection.commit()
            
            lines = self.cursor.rowcount

            self.cursor.close()
            self.connection.close()
            
            return(lines)
        
        else:
            return ("Erro")
    
    def delete(self, sql, id ):
        
        if (self.connectBdError == 0):
            
            self.cursor.execute(sql, id)
            self.connection.commit()
            
            lines = self.cursor.rowcount

            self.cursor.close()
            self.connection.close()
            
            return(lines)
        
        else:
            return ("Erro")

