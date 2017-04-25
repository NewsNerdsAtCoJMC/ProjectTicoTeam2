"""studentsonly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from apartments import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.buildingList, name='buildingList'),
    url(r'^building/(?P<building_slug>[-\w]+)', views.building, name='building'),
    #url(r'^apartments/(?P<apartment_slug>[-\w]+)', views.apartmentListing, name='apartment'),
    url(r'^apartments/listing/(?P<listing_id>[-\w]+)', views.apartmentDetail, name='detail'),
    url(r'^post-your-listing/$', views.postlisting, name='postlisting'),
    url(r'^post-your-review/$', views.postreview, name='postreview'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
