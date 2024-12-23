from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from GestBiblio import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil_page, name='accueil_page'),
    path('Contact/', views.Contact_page, name='Contact_page'),
    path('inscription/', views.inscription_page, name='inscription_page'),
    path('seconnecter/', views.seconnecter_page, name='seconnecter_page'),

    path('auteurs/', include('auteurs.urls')),
    path('livres/', include('livres.urls')),
    path('emprunts/', include('emprunts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
