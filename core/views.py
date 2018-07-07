from django.views.generic import (
    ListView, DetailView,
)

from core.models import Model

class ModelDetail(DetailView):
    model = Model

class ModelList(ListView):
    model = Model
