
import matplotlib.pyplot as plt

def plot_forecast(original, forecast, title="Sales Forecast"):
    plt.figure(figsize=(10, 4))
    plt.plot(original[-60:], label='Historical')
    plt.plot(forecast.index, forecast.values, label='Forecast')
    plt.title(title)
    plt.legend()
    plt.show()
