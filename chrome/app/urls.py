from django.urls import path
from . import views
urlpatterns=[
    path('',views.chrome_login),
    path('chrome_login1/', views.chrome_login1, name='chrome_login1'),
    path('home/',views.home,name='home'),
    path('intro',views.intro),
    path('chrome_logout',views.chrome_logout,name='chrome_logout'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('edit/<pid>',views.edit,name='edit'),
    path('delete/<pid>',views.delete,name='delete'),
    path('bookings/',views.bookings,name='bookings'),



    path('register/',views.register),
    path('user_home',views.user_home ,name='user_home'),
    path('view_pro/<pid>',views.view_pro,name='view_pro'),
    path('add_to_cart/<int:pid>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('user_buy/<cid>',views.user_buy,name='user_buy'),
    path('user_buy1/<pid>',views.user_buy1,name='user_buy1'),
    path('user_bookings',views.user_bookings,name='user_bookings'),
    path('user_buy/<int:cid>/', views.user_buy, name='user_buy'),
    path('order/', views.order_create, name='order_create'),
    path('order/success/', views.order_success, name='order_success'),
    
]
