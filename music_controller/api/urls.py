from django.urls import path
from .views import RoomView, CreateRoom

urlpatterns = [
    path('room/', RoomView.as_view()),
    path('new/', CreateRoom.as_view()),
]
