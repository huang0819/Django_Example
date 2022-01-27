# Create your views here.
from lunch.models import UserProfile, Menu, Recipe, MenuRecipe
from lunch.serializers import UserProfileSerializer, MenuSerializer, RecipeSerializer, MenuRecipeSerializer
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = Menu.objects.all()
        user_id = self.request.query_params.get('user_id', '')
        eat_date = self.request.query_params.get('eat_date', '')

        query = None

        if user_id:
            query = query | Q(eat_date=eat_date) if query else Q(
                user_id=user_id)
        elif eat_date:
            query = query | Q(eat_date=eat_date) if query else Q(
                eat_date=eat_date)

        return queryset if query is None else queryset.filter(query)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class MenuRecipeView(APIView):
    def get(self, request, format=None):
        menu_recipes = MenuRecipe.objects.all()
        serialize = MenuRecipeSerializer(menu_recipes, many=True)

        return Response({
            'status': 0,
            'data': serialize.data
        })

    def post(self, request, format=None):
        data = request.data
        serializer = MenuRecipeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': 0,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({
            "message": "Got some data!",
            "data": request.data,
        }, status=status.HTTP_200_OK)
    return Response({
        "message": "Hello, world!"
    })
