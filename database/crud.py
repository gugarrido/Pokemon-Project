import sqlite3
from sqlite3 import Error

class Crud:
    def __init__ (self):
        self.conn = None

    def get_conn(self, db_file):
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(db_file)
                self.conn.commit()
            except Error as e:
                print(e)
        return self.conn


    def check_existent(self, pokename):
        result = ''
        pokemon = ''
        pokeid = ''
        sql = f'''SELECT name,pokeid, height, weight, poketype FROM pokemons WHERE name="{pokename}"'''
        try:
            c = self.conn.cursor()
            result = c.execute(sql).fetchall()
            for row in result:
                pokemon = row[0]
                pokeid = row[1]
                pokeheight = row[2]
                pokeweight = row[3]
                poketype = row[4]
        except Error as e:
            print(e)

        if result:
            return {
                'status': 200,
                'pokemon': pokemon,
                'pokemon_id': pokeid,
                'pokemon_height': pokeheight,
                'pokemon_weight': pokeweight,
                'pokemon_type': poketype


            }
        else: 
            return {
                'status': 403
            }
        


    def insert_data(self, pokename, pokeid, height, weight, poketype):
        result = ''
        sql = f"INSERT INTO pokemons (name, pokeid, height, weight, poketype) VALUES ('{pokename}', '{pokeid}', '{height}', '{weight}', '{poketype}');"
        try:
            c = self.conn.cursor()
            result = c.execute(sql).fetchall()
            self.conn.commit()
        except Error as e:
            print(e)
        print(f"Command executed successfully:\n{sql}")
        return {
            'status': 200,
            'message': "Inserted data to the database"
        }


    def execute_select(self, table):
        result = ''
        sql = f"SELECT * FROM {table}"
        try:
            c = self.conn.cursor()
            result = c.execute(sql).fetchall()
            self.conn.commit()
        except Error as e:
            print(e)
        print(f"{sql}\n{result}")


    def execute_sql(self, sql):
        result = ''
        try:
            c = self.conn.cursor()
            result = c.execute(sql).fetchall()
            self.conn.commit()
        except Error as e:
            print(e)
        print(f"{sql}\n{result}")
        return filter(None, result)





