
import alpaca_trade_api as tradeapi

def send_order(api, symbol, qty, side, order_type="market", time_in_force="gtc"):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=order_type,
            time_in_force=time_in_force
        )
        print(f"Order submitted: {order}")
    except tradeapi.rest.APIError as e:
        print(f"Error submitting order: {e}")
