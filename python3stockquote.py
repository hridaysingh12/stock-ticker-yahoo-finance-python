# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:58:17 2022

@author: hrida
"""



import requests
import json

   
api_key_input = input("Enter API Key: ")  
api_key_input = api_key_input.strip()


user_input = input("Enter a ticker or multiple tickers (seperated by commas): ")

user_input = user_input.strip().upper().split(",")
user_input = [ticker.strip() for ticker in user_input]

        
     
quotes_string = ", ".join(user_input)
 
 
url = "https://yfapi.net/v6/finance/quote"
 
for ticker in user_input:
    try:
        querystring = {"symbols":ticker}
        
        headers = {
            'x-api-key': api_key_input
            }
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        # print(response.text)
        
        
        your_json = response.text
        parsed = json.loads(your_json)
        print(parsed["quoteResponse"]["result"][0]["longName"] +" : "+ str(parsed["quoteResponse"]["result"][0]['regularMarketPrice']))
    except:
        print("Error: " +ticker +" is not a valid ticker")
   
