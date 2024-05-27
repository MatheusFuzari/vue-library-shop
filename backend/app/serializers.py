from rest_framework.serializers import ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField, StringRelatedField
from django.contrib.auth.models import Group
from .models import *


class CustomUserSerializer(ModelSerializer):
    groups = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name',
                  'email', 'groups', 'user_permissions', )
        many = True


class AuthorReadSerializer(ModelSerializer):
    userFK = CustomUserSerializer()

    class Meta:
        model = Author
        fields = '__all__'
        many = True


class AuthorWriteSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        many = True


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        many = True


class BookReadSerializer(ModelSerializer):
    author = AuthorReadSerializer()

    categoryFK = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'
        many = True


class BookWriteSerializer(ModelSerializer):
    categoryFK = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'
        many = True


class LoanReadSerializer(ModelSerializer):
    userFK = CustomUserSerializer()
    bookFK = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Loan
        fields = '__all__'
        many = True


class LoanWriteSerializer(ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        many = True
