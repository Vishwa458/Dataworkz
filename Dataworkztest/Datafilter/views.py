from django.shortcuts import render
from .serializers import StockSerializer
from .models import Stock
from rest_framework import viewsets

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
