from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('service/',views.service),
    path('Registration/',views.Registration),
    path('faqs/',views.faqs),
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('history/',views.bookinghistory),
    path('allservices/',views.allservices),
    path('booknow/',views.booknow),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]