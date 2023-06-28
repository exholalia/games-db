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

# Backup the database
def backup():
    # Get the new backup number
    i = 1
    while os.path.isfile(f"games.db.bak{i}"):
        i += 1
    f = os.rename("games.db", f"games.db.bak{i}")
    logging.debug(f"Backed up games.db to games.db.bak{i}: {f}")

# Reset the database
def reset():
    backup()
    
    db = GamesDatabase()
    for definition in os.listdir("table_definitions"):
        os.system(f"sqlite3 games.db < table_definitions/{definition}")
    
    
if __name__ == "__main__":
    print("Are you sure you want to reset the database (a backup will be made)? (y/n)")
    r = input()
    
    if (r == "y"):
        reset()