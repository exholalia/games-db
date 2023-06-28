import logging, sqlite3
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