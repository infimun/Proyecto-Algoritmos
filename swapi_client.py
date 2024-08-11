import requests

class SWAPIClient:
    BASE_URL = 'https://www.swapi.tech/api/'

    @staticmethod
    def fetch_data(endpoint):
        response = requests.get(SWAPIClient.BASE_URL + endpoint)
        if response.status_code == 200:
            json_response = response.json()
            if 'result' in json_response:
                return json_response['result']
            elif 'results' in json_response:
                return json_response['results']
            else:
                print("Unexpected response structure:", json_response)
                raise KeyError('result or results')
        else:
            raise Exception('API request failed')

    @staticmethod
    def get_movies():
        return SWAPIClient.fetch_data('films')

    @staticmethod
    def get_species():
        return SWAPIClient.fetch_data('species')

    @staticmethod
    def get_planets():
        return SWAPIClient.fetch_data('planets')

    @staticmethod
    def search_character(query):
        return SWAPIClient.fetch_data(f'people/?search={query}')