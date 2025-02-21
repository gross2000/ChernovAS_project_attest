from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsActiveEmployee
from django_filters import rest_framework as django_filters
from .models import Factory, RetailNetwork, Entrepreneur
from .serializers import FactorySerializer, RetailNetworkSerializer, EntrepreneurSerializer


def home(request):
    return render(request, 'retailnet/home.html')

class FactoryFilter(django_filters.FilterSet):
    class Meta:
        model = Factory
        fields = ['country']

class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = FactoryFilter
    permission_classes = [IsActiveEmployee]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_fields = ['country']
    permission_classes = [IsActiveEmployee]


class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_fields = ['country']
    permission_classes = [IsActiveEmployee]