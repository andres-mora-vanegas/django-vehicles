from .models import State
from .serializers import StateSerializer
from rest_framework import routers, serializers, viewsets

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
