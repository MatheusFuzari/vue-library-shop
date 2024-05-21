from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
import datetime
from .serializers import *
# Create your views here.

class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LoanView(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        userId = self.request.user.id
        userHasLoans = Loan.objects.filter(userFK = userId).filter(deliverDate__gte = datetime.date() or deliverDate__is)

        return super().create(request, *args, **kwargs)