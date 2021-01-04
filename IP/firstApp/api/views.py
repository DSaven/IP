from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializer import CarSpecsSerializer
from firstApp.models import CarSpecs


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    # print(request.query_params)
    return Response({'message': "we received"})


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs


