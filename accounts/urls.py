from django.urls import path
from .views import logout,login,register,activate,dashboard,forgotPassword,resetPasswordValidate,resetPassword

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('',dashboard,name='dashboard'),
    path('forgotPassword/',forgotPassword,name='forgotPassword'),
    path('resetPasswordValidate/<uidb64>/<token>/',resetPasswordValidate,name='resetPasswordValidate'),
    path('resetPassword/',resetPassword,name='resetPassword'),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    
]
