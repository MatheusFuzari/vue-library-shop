from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('custom-user', CustomUserView)
router.register('authors', AuthorView)
router.register('category', CategoryView)
router.register('book', BookView)
router.register('loan', LoanView)

urlpatterns = router.urls
