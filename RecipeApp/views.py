from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm, AddIngredientsForm, AddInstructionsForm

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_form = AddIngredientsForm(request.POST)
        instruction_form = AddInstructionsForm(request.POST)

        if recipe_form.is_valid() and ingredient_form.is_valid() and instruction_form.is_valid():
            recipe = recipe_form.save()

            # Process ingredients
            ingredients = ingredient_form.cleaned_data['ingredients'].splitlines()
            for ingredient_name in ingredients:
                ingredient_name = ingredient_name.strip()  # Clean up any extra spaces
                if ingredient_name:
                    Ingredient.objects.create(recipe=recipe, name=ingredient_name)

            # Process instructions
            instructions = instruction_form.cleaned_data['instructions'].splitlines()
            for i, instruction_text in enumerate(instructions, start=1):
                instruction_text = instruction_text.strip()  # Clean up extra spaces
                if instruction_text:
                    Instruction.objects.create(recipe=recipe, step_number=i, instruction=instruction_text)

            return redirect('home')
    else:
        recipe_form = RecipeForm()
        ingredient_form = AddIngredientsForm()
        instruction_form = AddInstructionsForm()

    return render(request, 'add_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'instruction_form': instruction_form,
    })

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all()
    instructions = recipe.instructions.all()
    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions,
    })

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('home')

def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(request, 'update_recipe.html', {'recipe_form': recipe_form, 'recipe': recipe})

