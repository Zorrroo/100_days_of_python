import requests
from pprint import pprint
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = os.environ.get("T_ENDPOINT")
TEQUILA_API_KEY = os.environ.get("T_API_KEY")
headers = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination(self, city_name):
        local_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        query = {
            "term": city_name,
        }
        response = requests.get(url=local_endpoint, headers=headers, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code
        # print(response)

    def get_price(self, origin_city_iata, destination_city_code, from_time, to_time):

        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        query = {
            "fly_from": origin_city_iata,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": "INR",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
