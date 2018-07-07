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
]
