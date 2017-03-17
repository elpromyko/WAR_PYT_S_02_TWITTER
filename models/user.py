from builtins import property
from models.clcrypto import *

class User(object):
    
    __id = None
    username = None
    __hashed_password = None
    email = None
    
    def __init__(self):
        self.__id = -1
        self.username = ""
        self.__hashed_password = ""
        self.email = ""
        
    @property
    def id(self):
        return self.__id
    
    @property
    def hashed_password(self):
        return self.__hashed_password
    
    def set_password(self, password):
        self.__hashed_password = password_hash(password)
        
    def save_to_db(self, cursor, cnx):
        if self.__id == -1:
            sql_query = """
            INSERT INTO Users(name, hashed_password, email) VALUES('{}', '{}', '{}')
            """.format(self.username, self.__hashed_password, self.email)
        
            cursor.execute(sql_query)
            cnx.commit()
            self.__id = cursor.lastrowid
            return True
    
    @staticmethod 
    def load_user_by_id(cursor, id):
        sql_query = """
            SELECT name, hashed_password, email FROM Users WHERE id={}
            """.format(id)
            
        cursor.execute(sql_query)
        data = cursor.fetchone()
        
        if data is not None:
            loaded_user = User()
            loaded_user.__id = id
            loaded_user.username = data[0]
            loaded_user.__hashed_password = data[1]
            loaded_user.email = data[2]
            return loaded_user
        else:
            return None
    @staticmethod    
    def load_all(cursor):
        sql_query = """
            SELECT id, name, hashed_password, email FROM Users
            """
        cursor.execute(sql_query)
        data = cursor.fetchall()
        
        result = []
        
        for row in data:
            user = User()
            user.__id = row[0]
            user.name = row[1]
            user.__hashed_password = row[2]
            user.email = row[3]
           
            result.append(user)
        return result
        
        
    def printInfo(self):
        print("Id: {} Name: {} Email: {}".format(self.__id, self.username, self.email))
    