from django.conf.urls import url
from cadastro_guerreiros.views import lista, adiciona


urlpatterns = [
    url(r'^home/$', lista, name='home'),
    url(r'^adiciona/$', adiciona.as_view(), name='adiciona'),
]
