from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_swagger_view(title='Nuri API')

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', schema_view),

    url(r'^api/token-auth', obtain_auth_token),
    url(r'^api/classes/', include('data.urls')),
    url(r'^api/registration/', include('registration.urls')),
]
