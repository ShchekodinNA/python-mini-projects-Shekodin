import requests

class FlightData:
    def __init__(self, end_point, apikey):
        self.end_point = end_point
        self.apikey = apikey
        self.headers = {
            "apikey": apikey,
            # "accept": "application/json"
        }
        self.addition_query = "locations/query"
        self.addition_search = "search"

    def get_iata_city(self, city_name:str):
        params = {
            "term": city_name,
            "locale": 'en-US',
            "location_types": "city"
        }
        lv_url = f"{self.end_point}/{self.addition_query}"
        return requests.get(url=lv_url,
                            headers=self.headers,
                            params=params)

    def get_flights(self,from_iata: str, to_iata: str, nights_in_min: int,
                    nights_in_max: int, srch_frm_dt: str, srch_to_dt: str,
                    childrens: int = 0, adults: int = 1):
        """all dates in dd/mm/yyyy formats. IATA - CITY"""
        lv_url = f"{self.end_point}/{self.addition_search}"
        params = {
            "fly_from": f"city:{from_iata}",
            "fly_to": f"city:{to_iata}",
            "date_from": srch_frm_dt,
            "date_to": srch_to_dt,
            "nights_in_dst_from": nights_in_min,
            "nights_in_dst_to": nights_in_max,
            "adults": adults,
            "children": childrens,
            "limit": 1
        }
        return requests.get(url=lv_url, headers=self.headers, params=params)
