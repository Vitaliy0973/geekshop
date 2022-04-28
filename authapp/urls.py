from django.urls import path
from authapp.views import LoginGBView, ProfileUpdateView, RegisterView, Logout


app_name = 'authapp'

urlpatterns = [
    # path('login/', login, name='login'),
    path('login/', LoginGBView.as_view(), name='login'),

    # path('register/', register, name='register'),
    path('register/', RegisterView.as_view(), name='register'),

    # path('logout/', logout, name='logout'),
    path('logout/', Logout.as_view(), name='logout'),

    # path('profile/', profile, name='profile'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    path('verify/<str:email>/<str:activate_key>/',
         RegisterView.verify, name='verify')

]
