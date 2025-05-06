from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import CustomLoginView


app_name = 'users'

urlpatterns = [
  path(
    'login/',
    CustomLoginView.as_view(
      redirect_authenticated_user=True,
      template_name='login.html',
      authentication_form=LoginForm

    ),
    name='login'),
  
  path(
    'logout/',
    auth_views.LogoutView.as_view(
      template_name='logout.html'
    ),
    name='logout'
  )
]