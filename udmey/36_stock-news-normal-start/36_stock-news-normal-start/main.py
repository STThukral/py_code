import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


#STEP 1:- stock market API
# To get free API key goto below link 
# https://www.alphavantage.co/ is stock market API
# API key: LUX769MK8MU5VOXQ
#STEP 2 :- Enter in Below URL and get the result e.f is for IBM
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LUX769MK8MU5VOXQ
#TSLA 
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=LUX769MK8MU5VOXQ

api_key = "LUX769MK8MU5VOXQ"
STOCK_NAME="TSLA"
COMPANY_NAME="Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#stock_params = {
#    "fucntion" : "TIME_SERIES_DAILY",
#    "symbol": STOCK_NAME,
#    "appkey" : api_key,
#    }

# not sure paramters not working so commnetd it and used all the value in URL itself
#response = requests.get(STOCK_ENDPOINT,params=stock_params)

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey=LUX769MK8MU5VOXQ")

response.raise_for_status() # rasie an exception if any
tesla_data=response.json()
#print(tesla_data)
# One way to  get Meta Data information is as below
tesla_metadata = tesla_data["Meta Data"]
#print (tesla_metadata)

# STEP 1:-

# Another way is to use dictonary comprehension
metadata_dict_comp ={meta_data:meta_data_info for (meta_data,meta_data_info) in tesla_data.items() if meta_data =="Meta Data"}
print(metadata_dict_comp["Meta Data"]["1. Information"])
#print(metadata_dict_comp["Meta Data"]["3. Last Refreshed"])
Last_Refreshed=metadata_dict_comp["Meta Data"]["3. Last Refreshed"]
print(f'yesterday_refresh_date : {Last_Refreshed}')
#
last_refreshed_dict_comp ={time_series:closing_stock for (time_series,closing_stock) in tesla_data.items() if time_series =="Time Series (60min)"} #date_time == Last_Refreshed}
#print(last_refreshed_dict_comp["Time Series (60min)"][Last_Refreshed])

yesterday_closing_stock = float(last_refreshed_dict_comp["Time Series (60min)"][Last_Refreshed]["4. close"])
print (f'yesterday_closing_stock : {yesterday_closing_stock}')
last_day_refresh_format = datetime.strptime(Last_Refreshed, "%Y-%m-%d %H:%M:%S")
day_before_yesterday_refresh_date = str(last_day_refresh_format -timedelta(days=1))
print(f' day_before_yesterday : {day_before_yesterday_refresh_date}')
#print(last_refreshed_dict_comp["Time Series (60min)"][day_before_yesterday_refresh_date])
day_before_yesterday_closing_stock = float(last_refreshed_dict_comp["Time Series (60min)"][day_before_yesterday_refresh_date]["4. close"])
print (f'day_before_yesterday_closing_stock : {day_before_yesterday_closing_stock}')

#STEP 2: -
# not sure which day stock has gone up or down, so to get poistive difference doing abs
stock_difference = abs(yesterday_closing_stock - day_before_yesterday_closing_stock)
print (f'stock_difference : {stock_difference}')


#STEP 3:-
#calcuate difference percentage
difference_perc = (stock_difference / yesterday_closing_stock) *100
print (f'difference_perc : {difference_perc}')


if difference_perc > 5:
    print (" Get news")
else:
    print("NO news")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#          Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    #     Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

