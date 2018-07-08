from django.views.generic import (
    ListView, DetailView,
)

from core.models import Model

class ModelDetail(DetailView):
    model = Model

class ModelList(ListView):
    model = Model

from core.models import Ticker

class TickerList(ListView):
    model = Ticker

class TickerDetail(DetailView):
    model = Ticker
