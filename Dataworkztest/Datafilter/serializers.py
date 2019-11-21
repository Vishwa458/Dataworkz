from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('Date','Open','High','Low','Close','Shares_Traded','Turnover_Rs_Cr')
