import mysql.connector as cn
from mysql.connector import errorcode

class SQlConnector:



    def __connect_db__(self):
        try:
            connection = cn.connect(host='127.0.0.1',
                                                database='person',
                                                user='root',
                                                password='root')
            return connection

        except cn.Error as err:
            print("Error while connecting to MySQL\n", err)

    def save_person(self, first_name, last_name):

        connection = self.__connect_db__()

        if connection.is_connected():
            cursor = connection.cursor()
            stmt = f'insert into person(first_name, last_name) values(\'{first_name}\', \'{last_name}\')'

            cursor.execute(stmt)
            connection.commit()
            result = cursor.fetchall()
            connection.close()
            return result

    def get_persons(self):
        connection = self.__connect_db__()

        if connection.is_connected():
            cursor = connection.cursor()
            stmt = 'select * from person'

            cursor.execute(stmt)

            result = cursor.fetchall()

            persons = []

            for row in result:
                persons.append({'first_name': row[0], 'last_name': row[1]})

            return persons

    





if __name__ == '__main__':
    connector = SQlConnector