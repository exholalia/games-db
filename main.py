import requests, json

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
    
    return response.json()[0]

# Get details of a particular game
def get_game_details(game_id):
    return igdb_request('/games', f'fields name, platforms; where id = {game_id};')

# Login to IGDB REST API
def init():
    global client_id, api_key, bearer_token, connection
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

def main():
    init()
    print(get_game_details(22704)['platforms'])
    

main()