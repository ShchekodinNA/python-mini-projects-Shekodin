import requests


class SheetyData:
    def __init__(self, token: str, api_end_point: str):
        self.api_end_point = api_end_point
        self.headers = {
            "Authorization": token
        }

    def get_rows(self):
        return requests.get(url=self.api_end_point, headers=self.headers)

    def post_rows(self, body_json: dict):
        return requests.post(url=self.api_end_point, headers=self.headers, json=body_json)

    def update_row(self, chng_rw_id: int, body_json: dict):
        new_url = f"{self.api_end_point}/{chng_rw_id}"
        return requests.put(url=new_url, headers=self.headers, json=body_json)

