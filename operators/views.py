from rest_framework import viewsets
from rest_framework.views import APIView, status

from .models import Operator
from .serializers import OperatorSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
    lookup_field = 'pk'
