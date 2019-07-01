from django.urls import path
from .views import (
    FundiListView,
    FundiDetailView,
    FundiCreateView,
    FundiUpdateView,
    FundiDeleteView,
    UserFundiListView
)
from . import views

urlpatterns = [
    path('', views.fundi, name='fundi'),
    path('fundi', FundiListView.as_view(), name='fundi'),
    path('user/<str:username>', UserFundiListView.as_view(), name='user-fundis'),
    path('fundi/<int:pk>/', FundiDetailView.as_view(), name='fundi-detail'),
    path('fundi/new/', FundiCreateView.as_view(), name='fundi-create'),
    path('fundi/<int:pk>/update/', FundiUpdateView.as_view(), name='fundi-update'),
    path('fundi/<int:pk>/delete/', FundiDeleteView.as_view(), name='fundi-delete'),
    
]