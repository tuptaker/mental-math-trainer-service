from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from mm_trainer_rest_api.serializers import UserSerializer, GroupSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the mental math trainer index.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer