from rest_framework.routers import DefaultRouter
from .views import TodolistView

router = DefaultRouter()
router.register(r'todolists', TodolistView, basename='todolist')

urlpatterns = router.urls