import requests
from flask import Flask
import json
app = Flask(__name__)


def get_config_info():
    try:
        with open("config.json") as fp:
            return json.load(fp)
    except:
        raise ValueError("Something went wrong")


@app.route('/get-weather/<string:zipcode>')
def get_weather(zipcode):
    config_info = get_config_info()
    endpoint = f"{config_info['endpoint']}?zip={zipcode},{config_info['country_code']}&APPID={config_info['apikey']}"
    print(endpoint)
    response =  requests.get(endpoint)
    print(response.status_code)
    if response.status_code == 200:
        return response.content
    else:
        return {'Error': 'No Data Found'}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")