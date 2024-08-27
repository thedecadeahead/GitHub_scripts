
def screen_stocks(engineered_data, min_price=1, max_price=1000, min_volume=100):
    screened_stocks = {}

    for symbol, df in engineered_data.items():
        mid_price = df['mid_price'].iloc[0]
        if min_price <= mid_price <= max_price:
            screened_stocks[symbol] = df

    return screened_stocks
