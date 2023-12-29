from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('add/',views.add,name="add"),
    path('addrec/',views.addrec,name="addrec"),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/delete/<int:id>/',views.delete,name='delete'),
    path('home/update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name='uprec'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

]