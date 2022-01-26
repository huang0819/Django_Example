from django.utils.timezone import now
from rest_framework import serializers
from lunch.models import UserProfile, Menu, Recipe, MenuRecipe
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)

    age = serializers.SerializerMethodField()
    BMI = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'birth_date', 'weight', 'height',
                  'user', 'age', 'BMI', 'user_id']

    def create(self, validated_data):
        user = validated_data.pop('user_id', None)
        user_profile = UserProfile.objects.create(
            user=user, **validated_data)
        return user_profile

    def update(self, instance, validated_data):
        instance.birth_date = validated_data.get(
            'birth_date', instance.birth_date)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)

        instance.save()
        return instance

    def get_age(self, instance):
        return now().year - (instance.birth_date).year

    def get_BMI(self, instance):
        return instance.weight / (instance.height/100)**2


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name']
        read_only_fields = ['created_at', 'created_at']


class MenuRecipeSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = MenuRecipe
        fields = ['recipes']


class MenuSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)
    recipe_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all(), write_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())

    class Meta:
        model = Menu
        fields = ['eat_date', 'recipes', 'user_id', 'recipe_ids']

    def create(self, validated_data):
        user = validated_data.pop('user_id', None)
        recipe_ids = validated_data.pop('recipe_ids', None)
        print(user)
        menu = Menu.objects.create(
            user=user, **validated_data)

        for recipe in recipe_ids:
            MenuRecipe.objects.create(menu=menu, recipe=recipe)

        return menu
