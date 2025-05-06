from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm


class CustomLoginView(LoginView):
  form_class = LoginForm


  def form_valid(self, form):

    self.request.session.modified = True

    return super(CustomLoginView, self).form_valid(form)