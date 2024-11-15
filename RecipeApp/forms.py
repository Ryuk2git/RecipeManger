from django import forms
from .models import Recipe, Ingredient, Instruction

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']

class AddIngredientsForm(forms.Form):
    ingredients = forms.CharField(widget=forms.Textarea, label="Ingredients (one per line)", required=True)

class AddInstructionsForm(forms.Form):
    instructions = forms.CharField(widget=forms.Textarea, label="Instructions (one per line)", required=True)
