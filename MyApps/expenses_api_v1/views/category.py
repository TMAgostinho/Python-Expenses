from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

#my imports
from expenses.models import Category
from expenses_api_v1.serializers import CategorySerializer

#Category Views
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))

class CategoryApiGeneric(APIView):

    @staticmethod
    def get(request, category_id = None):
        if not IsAuthenticated:
            return Response('Wrong credentials', status=status.HTTP_401_UNAUTHORIZED)

        if category_id == None:
            serializer = CategorySerializer(Category.objects.all(), many=True)
            return Response(serializer.data)
        else:
            category = get_object_or_404(Category, pk=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
