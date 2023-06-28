import logging, sys
from igdb import IGDB
from games_db import GamesDatabase

def main():
    # Set logging level
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
    
    # Setup connections
    games_db = GamesDatabase()
    igdb = IGDB()
    
    print(igdb.get_platforms_details())
    
    games_db.cleanup()

if __name__ == "__main__":
    main()