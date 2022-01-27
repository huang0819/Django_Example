from unicodedata import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lunch import views

router = DefaultRouter()

router.register(r'userProfiles', views.UserProfileViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'menuRecipes', views.MenuRecipeView.as_view()),
]
