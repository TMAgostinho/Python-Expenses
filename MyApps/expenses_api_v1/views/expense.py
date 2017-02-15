from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core import serializers

#my imports
from expenses.models import Expense
from expenses_api_v1.serializers import ExpenseSerializer

#Expenses Views
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))

class ExpenseApiGeneric(APIView):

    @staticmethod
    def get(request, expense_id = None):
        if not IsAuthenticated:
            return Response('Wrong credentials', status=status.HTTP_401_UNAUTHORIZED)

        if expense_id == None:
            serializer = ExpenseSerializer(Expense.objects.filter(user = request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = ExpenseSerializer(get_object_or_404(Expense, pk=expense_id, user=request.user))
            return Response(serializer.data)

    @staticmethod
    def post(request):
        if not IsAuthenticated:
            return Response('Wrong credentials', status=status.HTTP_401_UNAUTHORIZED)

        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)