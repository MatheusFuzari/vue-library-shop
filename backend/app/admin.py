from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Teste)
admin.site.register(Relation)