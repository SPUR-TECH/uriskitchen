from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('meal/', views.meal_view, name='meal_view'),
    path('meal/<int:pk>/', views.mealDetailView.as_view(), name='meal_detail'),
    path('comment-create/<int:pk>', views.commentCreateView.as_view(), name='comment_create'),
    path('comment-update/<int:pk>/', views.commentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', views.commentDeleteView.as_view(), name='comment_delete'),
    path('dessert/', views.dessert_view, name='dessert_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('success/', views.success_view, name='success_view'),
]
