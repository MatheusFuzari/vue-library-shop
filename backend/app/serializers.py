from rest_framework.serializers import ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField
from .models import *

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True
    
class AuthorSerializer(ModelSerializer):
    userFK = CustomUserSerializer()
    class Meta:
        model = Author
        fields = '__all__'
        many = True

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        many = True

class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    categoryFK = SlugRelatedField(
        many = True,
        read_only = True,
        slug_field= 'name'
    )
    class Meta:
        model = Book
        fields = '__all__' 
        many = True

class LoanSerializer(ModelSerializer):
    #userFK = CustomUserSerializer()
    #bookFK = BookSerializer()
    class Meta:
        model = Loan
        fields = '__all__'
        many = True
