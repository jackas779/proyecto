from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import Home, LoginView, SignUpView
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('', Home.as_view(), name="index"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', SignUpView.as_view(), name="register"),
    path('inv/', include('inv.urls')),
    path('mov/', include('mov.urls')),
    path('profile/', include('user.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)