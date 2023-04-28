from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path, include
from comparis_web import views
from comparis_web.forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('login',
         LoginView.as_view(template_name='login.html', success_url='home', authentication_form=CustomLoginForm),
         name='login'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('signup', views.signup, name='signup'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("properties_views/", login_required(views.properties_views), name="properties_views"),
    path("detail_view/<int:id>/", login_required(views.detail_view), name="detail_view"),
]
