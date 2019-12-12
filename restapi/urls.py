from django.urls import path

from cake.views import CakeView, CakeDetailView


urlpatterns = [
    path('cakes', CakeView.as_view()),
    path('cakes/<int:id>', CakeDetailView.as_view()),
]
