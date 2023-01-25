from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
import random
import ast
# defino la función index, la estamos usando en urls

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
recipes_all = list(Recipe.objects.all())

def search_ingredients(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched == '':
            recipes = []
        else:
            recipes = Recipe.objects.all().filter(ingredients__contains=searched)
            recipes = list(recipes)
            for recipe in recipes:
                if recipe.ingredients[0] == '{':
                    recipe.ingredients = list(ast.literal_eval(recipe.ingredients))
                else: 
                    recipe.ingredients = list(recipe.ingredients)        
        return render(request, 'search_ingredients.html', {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'search_ingredients.html', {})
    
def get_random_recipes(all):
    return random.sample(all, 5)

def index(request):
    recipes = get_random_recipes(recipes_all)
    
    for recipe in recipes:
        print(recipe.ingredients[0])
        print(type(recipe.ingredients))
        if recipe.ingredients[0] == '{':
            recipe.ingredients = list(ast.literal_eval(recipe.ingredients))
        else: 
            recipe.ingredients = list(recipe.ingredients)
        print(type(recipe.ingredients))
        
    days_recipes = zip(days, recipes)

    args = {"days_recipes": days_recipes}
    
    # le decimos que me renderee index html cuando se llame a la funcion index
    return render(request, 'index.html', args)