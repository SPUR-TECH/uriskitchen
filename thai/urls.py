from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('dessert/', views.dessert_view, name='dessert_view'),
    path('dessert/<int:pk>/', views.dessertDetailView.as_view(), name='dessert_detail'),
    path('dessert-comment-create/<int:pk>', views.dessertCommentCreateView.as_view(), name='dessert_comment_create'),
    path('dessert-comment-update/<int:pk>/', views.dessertCommentUpdateView.as_view(), name='dessert_comment_update'),
    path('dessert-comment-delete/<int:pk>/', views.dessertCommentDeleteView.as_view(), name='dessert_comment_delete'),
    path('meal/', views.meal_view, name='meal_view'),
    path('meal/<int:pk>/', views.mealDetailView.as_view(), name='meal_detail'),
    path('comment-create/<int:pk>', views.commentCreateView.as_view(), name='comment_create'),
    path('comment-update/<int:pk>/', views.commentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', views.commentDeleteView.as_view(), name='comment_delete'),
    path('cart/', views.cart_view, name='cart_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('success/', views.success_view, name='success_view'),
]
