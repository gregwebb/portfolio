from django import template

register = template.Library()

import os
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
from iexfinance import Stock
from iexfinance import get_historical_data

@register.filter
def price(ticker):
    try:
        ticker = Stock(ticker.ticker)
        price = ticker.get_price()
    except:
        return "---"
    else:
        return price

@register.filter
def plot(ticker):
    end = datetime.now()
    start = end.replace(end.year - 1)
    results_dir = os.path.join('static/tickerimages/')
    try:
        df = get_historical_data(ticker.ticker, start=start, end=end, output_format='pandas')
    except:
        Path(results_dir  + ticker.ticker + '.png' ).touch()
        return "---"
    else:
        data = df["close"].tolist()
        fig = plt.figure(figsize=( .9,.35))
        rect = fig.patch
        rect.set_facecolor('#000000')
        plt.plot(data, linewidth=.35, color="blue")
        plt.axis('off')
        plt.savefig(results_dir + ticker.ticker + '.svg')
        plt.gcf().clear()
        return ""

@register.filter
def plot_detail(ticker):
    end = datetime.now()
    start = end.replace(end.year - 1)
    yearago = (str(start.day) + "/" + str(start.month) + "/" + str(start.year))
    today = (str(end.day) + "/" + str(end.month) + "/" + str(end.year))
    results_dir = os.path.join('static/tickerimages/')
    try:
        df = get_historical_data(ticker.ticker, start=start, end=end, output_format='pandas')
    except:
        Path(results_dir  + ticker.ticker + '.png' ).touch()
        return "---"
    else:
        plt.plot(df["close"], linewidth=1, color="blue")
        plt.axis('auto')
        plt.ylabel('Price (US Dollars)')
        plt.xticks([1,252],[yearago,today])
        plt.savefig(results_dir + ticker.ticker + '_detailed.svg')
        plt.gcf().clear()
