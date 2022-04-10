import requests


class PixelaWork:
    def __init__(self, username, token, graph_id):
        self.end_point = "https://pixe.la/v1/users"
        self.username = username
        self.token = token
        self.graph_id = graph_id
        self.header = {
            "X-USER-TOKEN": self.token
        }
        self.get_pixel_url = f"{self.end_point}/{self.username}/graphs/{self.graph_id}"
        self.post_pixel_url = f"{self.end_point}/{self.username}/graphs/{self.graph_id}"
        self.update_pixel_url = self.get_pixel_url

    def get_pixel(self, YYYYmmdd: str):
        url = f"{self.get_pixel_url}/{YYYYmmdd}"
        return requests.get(url=url, headers=self.header)

    def post_pixel(self, YYYYmmdd: str, quantity):
        params = {
            "date": YYYYmmdd,
            "quantity": str(quantity)
        }
        return requests.post(url=self.post_pixel_url, headers=self.header, json=params)

    def update_pixel(self, YYYYmmdd: str, addquant):
        geted_pixel = self.get_pixel(YYYYmmdd).json()
        if "quantity" in geted_pixel:
            all_quant = int(geted_pixel["quantity"]) + addquant
        else:
            all_quant = addquant
        return self.post_pixel(YYYYmmdd=YYYYmmdd, quantity=all_quant)
