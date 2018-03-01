from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from mm_trainer_django import settings
from mm_trainer_rest_api import views
from rest_framework import routers
from allauth.account.views import confirm_email
from mm_trainer_rest_api.views import UserViewSet, django_rest_auth_null, VerifyEmailView

from allauth.account.views import confirm_email as allauthemailconfirmation
import regex
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^rest-auth/registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^rest-auth/registration/account-confirm-email/', views.null_view, name='account_confirm_email'),
    path('rest-auth/registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    #url(r'^rest-auth/registration/verify-email/(?P<key>\w+)/$', confirm_email, name="account_confirm_email"),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/account-confirm-email/(?P<key>{0})/$', TemplateView.as_view(template_name='empty.html'), name='account_confirm_email'),
    path('api/', include('mm_trainer_rest_api.urls')),
    url(r'^rest-auth/registration', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)