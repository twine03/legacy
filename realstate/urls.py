from django.conf.urls import include, url

from django.contrib.auth.decorators import login_required
from realstate.views import *

urlpatterns = [
    url(r'^$', index.as_view(), name='index'),
    url(r'^property/', show_propiedad.as_view(), name="propiedad"),
    url(r'^send_mail/', enviar_mail.as_view(), name="enviar_email"),
]