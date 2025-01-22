from django.urls import path
from . import views
urlpatterns=[
    path('',views.chrome_login),
    path('chrome_login1',views.chrome_login),
    path('home',views.home),
    path('intro',views.intro),
    path('chrome_logout',views.chrome_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),



    path('register',views.register),
    path('user_home',views.user_home),
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('delete_cart/<id>',views.delete_cart),
    path('user_buy/<cid>',views.user_buy),
    path('user_buy1/<pid>',views.user_buy1),
    path('user_bookings',views.user_bookings),
    path('bookings',views.bookings),
]