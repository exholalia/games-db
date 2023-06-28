import logging, requests, sys


class IGDB:
    client_id = None
    bearer_token = None

    # Request information from IGDB
    def igdb_request(self, url_endpoint, query):
        logging.debug(f"client-id: {self.client_id}, bearer-token: {self.bearer_token}")
        headers = {
            'Content-Type': 'application/json',
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.bearer_token}'
        }
        
        # Make the request
        response = requests.post(
            f'https://api.igdb.com/v4{url_endpoint}',
            headers=headers,
            data=query
        )
        
        return response.json()

    # Get details of a particular game
    def get_game_details(self, game_id):
        return self.igdb_request('/games', f'fields name, platforms; where id = {game_id};')[0]

    # Get details of all platforms
    def get_platforms_details(self):
        return self.igdb_request('/platforms', f'fields id, name; limit 500;')

    # Login to IGDB REST API
    def login(self):
        # Get the client ID and API key from the text files  
        f = open('api_keys/igdb_client_id.txt', 'r')
        self.client_id = f.readline().rstrip()
        f.close()
        
        f = open('api_keys/igdb_api_key.txt', 'r')
        api_key = f.readline().rstrip() # This doesn't need to be stored in the object
        f.close()
        
        # Login to IGDB
        login_response = requests.post(
            f'https://id.twitch.tv/oauth2/token?client_id={self.client_id}&client_secret={api_key}&grant_type=client_credentials'
        )
        
        login_response.raise_for_status()
        
        # Get the access token from the response
        self.bearer_token = login_response.json()['access_token']
        logging.debug(f"Bearer token: {self.bearer_token}")
        
    def __init__(self):
        self.login()