from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = "hello-viewset") ## use base name where there's no queryset
router.register('profile', views.UserProfileViewSet) ## otherwise django can figure it out by the model name in queryset

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path("", include(router.urls))
]