from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^employee/$',views.employeeApi),
    
    url(r'^SaveFile$', views.SaveFile)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)