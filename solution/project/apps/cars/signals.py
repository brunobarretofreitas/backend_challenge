from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Car, Tyre


@receiver(post_save, sender=Car)
def create_tyres_for_new_car(sender, instance, created=False, **kwargs):
    if created:
        Tyre.objects.bulk_create([Tyre(car=instance)] * 4)
