import requests
import time

def check_price(coin, upper_threshold, lower_threshold):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()[coin]['usd']
        if price > upper_threshold:
            print(f"ALERT: {coin.upper()} price above {upper_threshold}! Current: ${price}")
        elif price < lower_threshold:
            print(f"ALERT: {coin.upper()} price below {lower_threshold}! Current: ${price}")
        else:
            print(f"{coin.upper()} price stable: ${price}")
    else:
        print("API request failed.")

if __name__ == "__main__":
    coin = 'bitcoin'
    upper = 70000
    lower = 50000
    while True:
        check_price(coin, upper, lower)
        time.sleep(60)  # Check every minute