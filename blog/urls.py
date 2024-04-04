from django.urls import path
from .views import ItemsListView, items_detail, download_qr_code
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', ItemsListView.as_view(), name="home"),
    path('<uuid:pk>', items_detail, name='items_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('items/<uuid:pk>/download_qr/', download_qr_code, name='download_qr_code'),
]
