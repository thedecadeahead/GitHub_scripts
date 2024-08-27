
import time
from alpaca_trade_api.rest import TimeFrame, APIError

def fetch_data(api, symbol='AAPL', days=360):
    data = {}
    retry_count = 3
    success = False

    while retry_count > 0 and not success:
        try:
            bars = api.get_bars(symbol, TimeFrame.Day, limit=days).df
            if bars.empty or 'close' not in bars.columns:
                print(f"Warning: No valid 'close' data for {symbol}")
                break
            
            data[symbol] = bars
            success = True
        except APIError as e:
            print(f"Error fetching data for {symbol}: {e}")
            retry_count -= 1
            if retry_count > 0:
                print(f"Retrying {symbol}... ({retry_count} retries left)")
                time.sleep(3)
            else:
                print(f"Skipping {symbol} due to repeated errors.")
                break
        except Exception as e:
            print(f"Unexpected error for {symbol}: {e}")
            break
        
    return data
