from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    path('createOrder/', views.create_order, name="createOrder"),
    path('updateOrder/<str:pk>/', views.update_order, name="updateOrder"),
    path('deleteOrder/<str:pk>/', views.delete_order, name="deleteOrder"),

    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('user/', views.home, name="user"),

]

