from rest_framework import serializers
from .models import Khodro

class KhodroSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    read_only_fields = ['brand_name']
    
    class Meta:
        model = Khodro
        fields = ['id', 'brand', 'brand_name', 'model', 'owner_name', 'owner_phone', 'pelak', 'created_date']
        
    def get_brand_name(self, obj):
        return obj.brand.title