from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import datetime
import json
from .serializers import *
# Create your views here.


class ReadWriteSerializerMixin(object):
    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class


class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.filter(id=user.id)
        print(queryset)
        return queryset


class AuthorView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Author.objects.all()
    write_serializer_class = AuthorWriteSerializer
    read_serializer_class = AuthorReadSerializer
    authentication_classes = (IsAuthenticated, )


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (IsAuthenticated, )


class BookView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Book.objects.all()
    write_serializer_class = BookWriteSerializer
    read_serializer_class = BookReadSerializer


class LoanView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Loan.objects.all()
    write_serializer_class = LoanWriteSerializer
    read_serializer_class = LoanReadSerializer
    authentication_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        try:
            body = request.body
            bodyJson = json.loads(body.decode('utf-8'))
            print(bodyJson)
            userHasLoans = Loan.objects.filter(
                userFK__id=bodyJson['userFK']).filter(deliverDate__isnull=True)
            qntBooks = len(userHasLoans.values('bookFK'))
            qntBooksReq = len(bodyJson['bookFK'])
            if ((qntBooks+qntBooksReq) <= 3):
                booksSaved = []
                for i in bodyJson['bookFK']:
                    bookAlreadyLoan = Loan.objects.filter(
                        userFK__id=bodyJson['userFK']).filter(deliverDate__isnull=True).filter(bookFK=i).values()
                    if (list(bookAlreadyLoan) != []):
                        booksSaved.append(False)
                    else:
                        booksSaved.append(True)
                if (False not in booksSaved):
                    return super().create(request, *args, **kwargs)
                return Response({"You've already loaned one of these books"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'You cant loan more books!'}, status=status.HTTP_400_BAD_REQUEST)
        except Loan.DoesNotExist:
            return Response({'Error when trying to save!'}, status=status.HTTP_404_NOT_FOUND)
