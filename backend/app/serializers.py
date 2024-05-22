from rest_framework.serializers import ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField, StringRelatedField
from .models import *

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True
       
    
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        many = True
        # extra_kwargs = {
        #     'photo': {
        #         'required': False,
        #     },
        #     'biography': {
        #         'required': False,
        #     },
        #     'userFK': {
        #         'required': False,
        #     },
        # }


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        many = True

class BookReadSerializer(ModelSerializer):
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

class BookWriteSerializer(ModelSerializer):    
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
    userFK = CustomUserSerializer()
    bookFK = BookReadSerializer()
    class Meta:
        model = Loan
        fields = '__all__'
        many = True


class RelationSerializer(ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'
        many = True

class TesteReadSerializer(ModelSerializer):
    relationFK = RelationSerializer()
    class Meta:
        model = Teste
        fields = '__all__'
        many = True

class TesteWriteSerializer(ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'
        many = True


    