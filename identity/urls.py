from django.urls import path
from .views import login_view, login_form_view

app_name = "identity"
urlpatterns = [
    path('custom-login/', login_view, name="custom-login"),
    path('custom-login-form/', login_form_view, name="custom-login-form"),
]
