import logging, requests, sqlite3, sys
from sqlite3 import Error

client_id = None
api_key = None
bearer_token = None
connection = None

# Request information from IGDB
def igdb_request(url_endpoint, query):
    headers = {
        'Content-Type': 'application/json',
        'Client-ID': client_id,
        'Authorization': f'Bearer {bearer_token}'
    }
    
    # Make the request
    response = requests.post(
        f'https://api.igdb.com/v4{url_endpoint}',
        headers=headers,
        data=query
    )
    
    return response.json()

# Get details of a particular game
def get_game_details(game_id):
    return igdb_request('/games', f'fields name, platforms; where id = {game_id};')[0]

# Get details of all platforms
def get_platforms_details():
    return igdb_request('/platforms', f'fields id, name; limit 500;')

# Create SQLite connections
def create_sqlite_connection():
    global connection
    if connection is not None:
        logging.info("Connection to SQLite Games DB already exists")
        return
    
    try:
        connection = sqlite3.connect("games.db")
        logging.debug("Connection to SQLite Games DB successful")
    except Error as e:
        logging.error(f"The error '{e}' occurred")

    return connection

# Login to IGDB REST API
def login():
    global client_id, api_key, bearer_token
    # Set up IGDB REST API connection
    # Get the client ID and API key from the text files  
    if (client_id is None):
        f = open('api_keys/igdb_client_id.txt', 'r')
        client_id = f.readline().rstrip()
        f.close()
    
    if (api_key is None):
        f = open('api_keys/igdb_api_key.txt', 'r')
        api_key = f.readline().rstrip()
        f.close()
    
    # Login to IGDB
    login_response = requests.post(
        f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={api_key}&grant_type=client_credentials'
    )
    
    login_response.raise_for_status()
    
    # Get the access token from the response
    bearer_token = login_response.json()['access_token']
    logging.debug(f"Bearer token: {bearer_token}")
    
def init():
    # Set logging level
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
    
    # Start setup
    login()
    create_sqlite_connection()
    
def cleanup():
    connection.close()

def main():
    init()
    print(get_platforms_details())
    
    cleanup()
    

main()