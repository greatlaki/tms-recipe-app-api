from core.models import Recipe
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Recipe)
def pre_delete_recipe(sender, **kwargs):
    print("You are about to delete something")


@receiver(post_delete, sender=Recipe)
def post_delete_recipe(sender, **kwargs):
    print("You have just deleted a recipe")
