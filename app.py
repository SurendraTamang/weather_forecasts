#!/usr/bin/python3
'''
Weather Forecasting Python Script
'''
import requests


from credentials import *


class WeatherForcastsCity:
    def __init__(self,location):
        self.location = location
        self.API_USER = API_USER
        self.API_KEY = API_KEY
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.details = self.get_weather_data_by_location()
    
    def get_weather_data_by_location(self):
        '''
        This provides the weather details by location
        '''
        r = requests.get(f'{self.base_url}q={self.location}&appid={self.API_KEY}')
        if r.status_code == 200:
            return r.json()
        else:
            return None

def main():
    print("The main file is called!!!")



if __name__ == '__main__':
    pokhara_weather = WeatherForcastsCity('pokhara')
    breakpoint()
    main()