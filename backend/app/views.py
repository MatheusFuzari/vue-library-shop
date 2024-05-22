from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
import datetime
from .serializers import *
# Create your views here.

class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        myUser = CustomUser.objects.get(id = self.request.user.id)
        return myUser

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
        try:
            userId = 1
            print(datetime.date.today())
            userHasLoans = Loan.objects.filter(userFK = userId).count();
            print(userHasLoans)
        except Loan.DoesNotExist:
            print("nenhum registro")

        return super().create(request, *args, **kwargs)