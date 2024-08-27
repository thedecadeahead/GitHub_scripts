# main.py

import logging
from data_fetcher import fetch_options_data
from feature_engineering import generate_features
from train_models import train_model
from cross_validation import perform_cross_validation
from predict_and_trade import execute_trades
from sentiment_analysis import analyze_sentiment
from multi_symbol_fetch import fetch_symbols_data
from risk_management import manage_risk
from save_model import save_trained_model
from load_model import load_existing_model
from backtest import backtest_strategy
from trade_execution import execute_order

# Setup logging
logging.basicConfig(
    filename='/Users/james.richardson/Library/CloudStorage/OneDrive-Personal/Desktop/python/Stock-o-tron/logs/main_log.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting the Stock-o-tron main workflow")

        # Step 1: Fetch options data
        options_data = fetch_options_data()
        logger.debug(f"Options data: {options_data}")

        # Step 2: Generate features for model training
        features = generate_features(options_data)
        logger.debug(f"Generated features: {features}")

        # Step 3: Train the model
        model = train_model(features)
        logger.info("Model training complete")

        # Step 4: Cross-validate the model
        cv_results = perform_cross_validation(model, features)
        logger.debug(f"Cross-validation results: {cv_results}")

        # Step 5: Backtest the strategy
        backtest_results = backtest_strategy(model, features)
        logger.debug(f"Backtest results: {backtest_results}")

        # Step 6: Analyze sentiment (optional)
        sentiment_data = analyze_sentiment()
        logger.debug(f"Sentiment analysis: {sentiment_data}")

        # Step 7: Manage risk
        manage_risk()

        # Step 8: Execute trades
        execute_trades(model)

        # Step 9: Save the trained model
        save_trained_model(model)

        logger.info("Stock-o-tron workflow completed successfully")
    except Exception as e:
        logger.error(f"An error occurred in the main workflow: {e}")
        raise

if __name__ == "__main__":
    main()