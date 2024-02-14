from django.urls import path

from users.views import show_username, login_logout

urlpatterns = [
    path('show-username/', show_username, name='show-username'),
    path('auth/', login_logout, name='auth')
]
