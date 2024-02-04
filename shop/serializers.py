from rest_framework import serializers
from .models  import *

class AuthSerializer(serializers.ModelSerializer):
    class Meta():
        model = Auth
        fields = "__all__"

class SaledSerializer(serializers.ModelSerializer):
    class Meta():
        model = Saled
        fields = "__all__"

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"

class ShopcardSerializer(serializers.ModelSerializer):
    class Meta():
        model = Shopcard
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Items
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta():
        model = Admin
        fields = "__all__"
