import requests


class ApiResponse:
    url = "https://covidtracking.com/api/"
    endpoint = "/v1/us/current.json"

    def __init__(self):
        pass

    def get_json(self, url=url, endpoint=endpoint):
        if str(requests.get(url+endpoint)) == "<Response [200]>":
            return requests.get(url+endpoint).json()
        else:
            print(f"Error has occurred. The response was: {requests.get(url+endpoint)}")

    def get_nr_positives(self):
        return self.get_json()[0]['positive']

    def get_nr_negatives(self):
        return self.get_json()[0]['negative']

    def get_nr_recovered(self):
        return self.get_json()[0]['recovered']


