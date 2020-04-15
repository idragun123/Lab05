from django.conf.urls import url
from .views import CatalogView

app_name = 'PhoneCatalog'
urlpatterns = [
    url(r'^$', CatalogView.as_view(), name='CatalogView-view')
]
