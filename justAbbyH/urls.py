from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/logout/', login_required(auth_views.LogoutView.as_view()), name="logout"),  # redirects to login url from settings.py
    path('', include('pages.urls')),
    path('stories/', include('stories.urls')),
    path('subscribe/', include('subscribe.urls')),
]

# DEBUG mode only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
