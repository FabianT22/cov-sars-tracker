import requests


class ApiResponse:
    url = "https://covidtracking.com/api/"
    endpoint_current = "/v1/us/current.json"
    endpoint_states = "/v1/states/current.json"

    def __init__(self):
        pass

    def get_json(self, url=url, endpoint=endpoint_current):
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

    def get_positive_state(self, state_code=None):
        response_data = self.get_json(endpoint=self.endpoint_states)
        for state_info in response_data:
            if state_info['state'] == state_code:
                return state_info['positive'], state_info['negative'], state_info['recovered'], state_info['hospitalizedCurrently'], state_info['death']
            else:
                print(f'The state code {state_code} was incorrect!')


if __name__ == "__main__":
    print(f'The number of positive cases: {ApiResponse().get_positive_state("AK")[0]}')


