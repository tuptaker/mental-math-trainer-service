from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from mm_trainer_django import settings
from mm_trainer_rest_api import views
from rest_framework import routers
from allauth.account.views import confirm_email as allauthemailconfirmation

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration', include('rest_auth.registration.urls')),
    path('api/', include('mm_trainer_rest_api.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', allauthemailconfirmation, name='account_confirm_email'),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)