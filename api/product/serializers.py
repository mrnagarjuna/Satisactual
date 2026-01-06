from rest_framework import serializers
from .models import MstProdCodes,MstProdDisclosures,MstProdDocs,MstPromoCodes

class MstProdCodesSerializer(serializers.ModelSerializer):
     class Meta:
        model = MstProdCodes
        fields = "__all__"

class MstProdDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstProdDisclosures
        fields = '__all__'
      
class MstProdDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstProdDocs
        fields = '__all__'

class MstPromoCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPromoCodes
        fields = '__all__'