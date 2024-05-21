from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.timezone import timedelta
from .manager import UserManager


# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField("E-mail address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class Author(models.Model):
    userFK = models.OneToOneField(CustomUser, related_name="CustomUserAuthor", on_delete=models.CASCADE)
    photo = models.TextField()
    biography = models.TextField()
    
    def __str__(self):
        return self.userFK.email

class Category(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name

BOOK_PLATFORM = [
    ('EBOOK', 'EBOOK'),
    ('FÍSICO','FÍSICO')
]

BOOK_STATUS = [
    ('APROVADO','APROVADO'),
    ('PENDENTE','PENDENTE'),
    ('CANCELADO','CANCELADO')
]

class Book(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    image = models.TextField(null=False, blank=False)
    description = models.TextField()
    pages = models.IntegerField()
    platform = models.CharField(max_length=60, choices=BOOK_PLATFORM)
    edition = models.CharField(max_length=120)
    author = models.ForeignKey(Author, related_name="authorBook", on_delete=models.CASCADE)
    publish_year = models.DateField(auto_now_add=False)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=BOOK_STATUS)
    qntInStock = models.IntegerField()
    categoryFK = models.ManyToManyField(Category, related_name="BookCategories")

    def __str__(self):
        return self.title

class Loan(models.Model):
    userFK = models.ForeignKey(CustomUser, related_name="userLoan", on_delete=models.CASCADE, null=False, blank=False)
    bookFK = models.ForeignKey(Book, related_name="bookLoan", on_delete=models.CASCADE, null=False, blank=True)
    loanDate = models.DateField(auto_now_add=True)
    expectedDate = models.DateField(null=True, blank=True)
    deliverDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bookFK.title

    def save(self, *args, **kwargs):
        self.expectedDate = self.loanDate + timedelta(weeks=2)
        super(Loan, self).save(*args, **kwargs)