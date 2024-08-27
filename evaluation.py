import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def max_drawdown(returns):
    cumulative = np.cumprod(1 + returns) - 1
    peak = np.maximum.accumulate(cumulative)
    drawdown = (peak - cumulative) / peak
    return np.max(drawdown)

def win_loss_ratio(predictions, actuals):
    wins = np.sum(predictions == actuals)
    losses = np.sum(predictions != actuals)
    return wins / losses if losses != 0 else float('inf')