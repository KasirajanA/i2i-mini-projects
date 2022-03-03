from rest_framework import serializers

from company.models import Company

class CompanySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        exclude = ['created_at', 'updated_at']


      