import logging, sqlite3, os
from sqlite3 import Error

class GamesDatabase:
    connection = None
    
    # Create SQLite connections
    def __init__(self):
        try:
            self.connection = sqlite3.connect("games.db")
            logging.debug("Connection to SQLite Games DB successful")
        except Error as e:
            logging.error(f"The error '{e}' occurred")
        
    # Close SQLite connections
    def cleanup(self):
        self.connection.close()
        
    def add_platform(self, platform):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO platforms (console_id, name) VALUES (?, ?)", (platform['id'], platform['name']))
        self.connection.commit()
        
    def add_platforms(self, platforms):
        for platform in platforms:
            self.add_platform(platform)
            
    def print_table(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# Backup the database if it exists
def backup():
    if os.path.isfile("games.db"):
        # Get the new backup number
        i = 1
        while os.path.isfile(f"games.db.bak{i}"):
            i += 1
        f = os.rename("games.db", f"games.db.bak{i}")
        logging.debug(f"Backed up games.db to games.db.bak{i}: {f}")

# Reset the database
def reset_games_db():
    backup()
    
    db = GamesDatabase()
    for definition in os.listdir("sql_scripts/table_definitions"):
        os.system(f"sqlite3 games.db < sql_scripts/table_definitions/{definition}")
    
    
if __name__ == "__main__":
    print("Are you sure you want to reset the database (a backup will be made)? (y/n)")
    r = input()
    
    if (r == "y"):
        reset_games_db()