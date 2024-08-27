import requests
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def fetch_options_data(symbol):
    logging.debug(f"Fetching options data for {symbol} using updated endpoint")

    url = f"https://paper-api.alpaca.markets/v2/options/contracts"
    headers = {
        "APCA-API-KEY-ID": "PKBPTQVAVZDKLMCBO9IU",
        "APCA-API-SECRET-KEY": "MKtaiWhYgyRCbCvgNYdume2MyhOqHFstBx8Dpcok"
    }
    params = {
        "underlying_symbols": symbol,
        "expiration_date_lte": "2024-09-27"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        logging.debug(f"Options data for {symbol} received successfully.")
        return response.json()
    else:
        logging.error(f"Failed to fetch options data for {symbol}: {response.status_code}")
        logging.error(f"Error: {response.text}")
        return None

if __name__ == "__main__":
    symbol = "SERV"
    options_data = fetch_options_data(symbol)
    if options_data:
        print(f"Options data for {symbol}: {options_data}")
    else:
        print(f"Failed to retrieve options data for {symbol}.")