from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Airport
from .serializers import AirportSerializer
from rest_framework import permissions


class AirportListView(ListCreateAPIView):

    serializer_class = AirportSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Airport.objects.all()
    


class AirportDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = AirportSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    #permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return Airport.objects.filter(created_by = self.request.user)
    

