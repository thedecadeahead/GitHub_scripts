import numpy as np

def backtest(models, data):
    results = {}
    for symbol, model in models.items():
        df = data[symbol]
        X = df[['ma5', 'ma20', 'rsi', 'returns']].values
        y_true = np.where(df['close'].shift(-1) > df['close'], 1, 0)
        predictions = model.predict(X)
        accuracy = np.mean(predictions == y_true)
        results[symbol] = accuracy
        print(f"Backtest accuracy for {symbol}: {accuracy:.2f}")
    return results