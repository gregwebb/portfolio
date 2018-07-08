from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('models',
        views.ModelList.as_view(),
        name='ModelList'),
    path('model/<int:pk>',
        views.ModelDetail.as_view(),
        name='ModelDetail'),
    path('tickers',
        views.TickerList.as_view(),
        name='TickerList'),
    path('ticker/<int:pk>',
        views.TickerDetail.as_view(),
        name='TickerDetail'),
]
