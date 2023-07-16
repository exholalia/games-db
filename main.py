import logging, sys
from igdb import IGDB
from games_db import GamesDatabase, reset_games_db

# Add all IGDB platforms to the database
def add_all_platforms(igdb, games_db):
    platforms = igdb.get_platforms_details()
    games_db.add_platforms(platforms)
    games_db.add_my_platforms()
    
    games_db.print_table("my_platforms")

def main():
    # Set logging level
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
    
    # Setup connections
    games_db = GamesDatabase()
    igdb = IGDB()
    
    #reset_games_db()
    add_all_platforms(igdb, games_db)
    
    games_db.cleanup()

if __name__ == "__main__":
    main()