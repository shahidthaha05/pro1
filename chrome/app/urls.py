from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)
urlpatterns=[
    path('',views.intro),
    path('chrome_login',views.chrome_login,name='chrome_login'),
    path('home/',views.home,name='home'),
    path('intro',views.intro),
    path('chrome_logout',views.chrome_logout,name='chrome_logout'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('edit/<pid>',views.edit,name='edit'),
    path('delete/<pid>',views.delete,name='delete'),
    path('bookings/',views.bookings,name='bookings'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('update_order_status/<int:order_id>/<str:new_status>/', views.update_order_status, name='update_order_status'),
    



    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='pass_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='pass_reset_complete'),



    path('register/',views.register,name='register'),
    path('verify_otp_reg',views.verify_otp_reg, name='verify_otp_reg'),
    path('user_home',views.user_home ,name='user_home'),
    path('view_pro/<pid>',views.view_pro,name='view_pro'),
    path('add_to_cart/<int:pid>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('user_buy/<cid>',views.user_buy,name='user_buy'),
    path('user_buy1/<pid>',views.user_buy1,name='user_buy1'),
    path('user_bookings/',views.user_bookings,name='user_bookings'),
    path('user_buy/<int:cid>/', views.user_buy, name='user_buy'),
    path('order/', views.order_create, name='order_create'),
    path('order/success/', views.order_success, name='order_success'),
    path('cancel_booking/<int:buy_id>/', views.cancel_booking, name='cancel_booking'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path("update_cart_quantity/", views.update_cart_quantity, name="update_cart_quantity"),
    path('payment/<int:order_id>/', views.payment_view, name='payment_page'),
]
