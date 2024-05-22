from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('customUser', CustomUserView)
router.register('authors', AuthorView)
router.register('category', CategoryView)
router.register('book', BookView)
router.register('loan', LoanView)
router.register('teste', TesteView)
router.register('relation', RelationView)

urlpatterns = router.urls
