from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.quantity}"


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
    step_number = models.IntegerField()
    instruction = models.TextField()
    step = models.CharField(max_length=255, blank=True, null=True)  # Example field


    def __str__(self):
        return f"Step {self.step_number}: {self.instruction}"

    class Meta:
        ordering = ['step_number']
