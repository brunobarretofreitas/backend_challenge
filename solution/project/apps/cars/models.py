from django.db import models


class Car(models.Model):
    name = models.CharField(
        max_length=100, null=False, blank=False, help_text="Car's name"
    )
    model = models.CharField(
        max_length=100, null=False, blank=False, help_text="Car's model"
    )
    year = models.PositiveIntegerField(
        null=False, help_text="Year of Fabrication"
    )
    total_gas_capacity = models.FloatField(
        null=False, help_text="Total Gas Capacity in liters"
    )
    current_gas_capacity = models.FloatField(
        null=False, default=0, help_text="Current Gas Capacity in %"
    )

    class Meta:
        ordering = ("id",)


class Tyre(models.Model):
    car = models.ForeignKey(
        Car, related_name="tyres", on_delete=models.SET_NULL, null=True
    )
    degradation = models.FloatField(
        null=False, default=0, help_text="Degradation Status in %"
    )

    class Meta:
        ordering = ("id",)
