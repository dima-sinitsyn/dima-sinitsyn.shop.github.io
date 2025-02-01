from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login/', views.UserloginView.as_view(), name='login'),
    path("registration/", views.UserRegisrationView.as_view(), name="registration"),
    # path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("profile/", views.profile, name="profile"),
    path("users_cart/", views.users_cart, name="users_cart"),
    path("logout/", views.logout, name="logout"),
]
  