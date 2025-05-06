
import statsmodels.api as sm
import pandas as pd

def train_arima_model(series, order=(1,1,1)):
    model = sm.tsa.ARIMA(series, order=order)
    fitted_model = model.fit()
    return fitted_model

def forecast(fitted_model, steps=30):
    return fitted_model.forecast(steps=steps)
