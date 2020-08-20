from rest_framework import viewsets, mixins

from .serializers import CarSerializer
from ..models import Car


class CarViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
