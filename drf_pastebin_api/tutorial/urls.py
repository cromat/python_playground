from django.conf.urls import url, include
from django.conf.urls import include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include('snippets.urls')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^schema/$', schema_view),
]