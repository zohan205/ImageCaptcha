from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from basicapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('', views.index, name='index'),
    path('challenge/', views.challenge, name='challenge'),
    path('edit/', views.edit, name='edit'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
