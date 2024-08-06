import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from abc import ABC, abstractmethod


# Strategy Pattern: Define an abstract base class for forecasting models
class ForecasterModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass


# Concrete Strategy: ARIMA Model
class ARIMAForecaster(ForecasterModel):
    def train(self, data):
        model = auto_arima(
            data["Returns"],
            start_p=1,
            start_q=1,
            max_p=5,
            max_q=5,
            m=1,
            start_P=0,
            seasonal=False,
            d=1,
            D=1,
            trace=True,
            error_action="ignore",
            suppress_warnings=True,
            stepwise=True,
        )
        p, d, q = model.order
        self.model = ARIMA(data["Returns"], order=(p, d, q))
        self.model_fit = self.model.fit()

    def predict(self, data):
        return self.model_fit.forecast(steps=1)[0]


# Concrete Strategy: Random Forest Model
class RandomForestForecaster(ForecasterModel):
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()

    def train(self, data):
        X = data.drop("Target", axis=1)
        y = data["Target"]
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)

    def predict(self, data):
        X_scaled = self.scaler.transform(data.reshape(1, -1))
        return self.model.predict(X_scaled)[0]


# Factory Pattern: Model Factory for creating different forecaster models
class ForecasterFactory:
    @staticmethod
    def get_forecaster(model_type):
        if model_type == "ARIMA":
            return ARIMAForecaster()
        elif model_type == "RandomForest":
            return RandomForestForecaster()
        else:
            raise ValueError(f"Unknown model type: {model_type}")


# Main Forecaster class using Composition
class StockForecaster:
    def __init__(self, symbol, start_date, end_date, model_type="ARIMA"):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.model = ForecasterFactory.get_forecaster(model_type)

    def fetch_data(self):
        print(
            f"Fetching data for {self.symbol} from {self.start_date} to {self.end_date}"
        )
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        print(f"Data fetched for {self.symbol}")
        self.data["Returns"] = self.data["Close"].pct_change()
        self.data["Target"] = self.data["Returns"].shift(-1)
        self.data = self.data.dropna()

    def add_features(self):
        # Add lag features
        for i in range(1, 6):
            self.data[f"Lag_{i}"] = self.data["Returns"].shift(i)

        # Add rolling mean and standard deviation
        self.data["Rolling_Mean_5"] = self.data["Returns"].rolling(window=5).mean()
        self.data["Rolling_Std_5"] = self.data["Returns"].rolling(window=5).std()

        # Add day of week and month
        self.data["Day_of_Week"] = self.data.index.dayofweek
        self.data["Month"] = self.data.index.month

        self.data = self.data.dropna()

    def train_model(self):
        self.model.train(self.data)

    def backtest(self, lookback_period=30):
        returns = []
        for i in range(lookback_period, len(self.data)):
            train_data = self.data.iloc[:i]
            test_data = self.data.iloc[i : i + 1]

            self.model.train(train_data)

            if isinstance(self.model, RandomForestForecaster):
                features = test_data.drop(["Target", "Returns"], axis=1).values[0]
            else:  # ARIMA
                features = train_data

            prediction = self.model.predict(features)
            returns.append(prediction)

        self.data["Predicted_Returns"] = pd.Series(
            returns, index=self.data.index[lookback_period:]
        )
        self.data["Strategy_Returns"] = self.data["Predicted_Returns"] * self.data[
            "Returns"
        ].shift(-1)

        cumulative_returns = (1 + self.data["Strategy_Returns"].fillna(0)).cumprod()
        sharpe_ratio = (
            np.sqrt(252)
            * self.data["Strategy_Returns"].mean()
            / self.data["Strategy_Returns"].std()
        )

        print(f"Cumulative Returns: {cumulative_returns.iloc[-1]}")
        print(f"Sharpe Ratio: {sharpe_ratio}")


def test_forecaster(model_type):
    forecaster = StockForecaster("AAPL", "2020-01-01", "2023-12-31", model_type)
    forecaster.fetch_data()
    forecaster.add_features()
    forecaster.train_model()
    forecaster.backtest()


if __name__ == "__main__":
    print("Testing ARIMA Forecaster:")
    test_forecaster("ARIMA")
    print("\nTesting Random Forest Forecaster:")
    test_forecaster("RandomForest")
