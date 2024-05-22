from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
import datetime
from .serializers import *
# Create your views here.

class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset. 
    """

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

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Book.objects.all()
    write_serializer_class  = BookWriteSerializer
    read_serializer_class  = BookReadSerializer

class LoanView(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        userId = self.request.user.id
        userHasLoans = Loan.objects.filter(userFK = userId).filter(deliverDate__gte = datetime.date() or deliverDate__is)

        return super().create(request, *args, **kwargs)
    
class RelationView(ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class TesteView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Teste.objects.all()
    write_serializer_class  = TesteWriteSerializer
    read_serializer_class  = TesteReadSerializer