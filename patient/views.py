from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *
from .filters import *
from rest_framework import status
from datetime import date
from django.db.models import Sum, F
from django.db import transaction
from common.exception_response import *
from common.pagination import *


@api_view(['GET', 'POST',])
def patient(request, *args, **kwargs):
    if request.method == "POST":
        data = request.data
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    instance = serializer.save()

                    response = {
                        "message": f'Patient succesfully created', "status": 'success'}
                    return Response(response)

            except Exception as e:
                return exception_handler(e)
        else:
            response = {
                "message": serializer.errors, "status": 'error'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        try:
            paginator = CustomPagination()
            paginator.page_size = 10
            queryset = Patient.objects.all()
            filter = PatientFilter(request.GET, queryset)
            result_page = paginator.paginate_queryset(filter.qs, request)
            response = PatientSerializer(
                result_page, many=True).data
            return paginator.get_paginated_response(response)
        except Exception as e:
            response = {
                "message": 'Error something went wrong', "status": 'error'}
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({})


@api_view(['GET', 'POST',])
def visit(request, *args, **kwargs):
    if request.method == "POST":
        data = request.data
        serializer = VisitSerializer(data=data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    instance = serializer.save()

                    response = {
                        "message": f'Visit succesfully created', "status": 'success'}
                    return Response(response)

            except Exception as e:
                return exception_handler(e)
        else:
            response = {
                "message": serializer.errors, "status": 'error'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        try:
            paginator = CustomPagination()
            paginator.page_size = 10
            queryset = Visit.objects.all()
            filter = VisitFilter(request.GET, queryset)
            result_page = paginator.paginate_queryset(filter.qs, request)
            response = VisitListSerializer(
                result_page, many=True).data
            return paginator.get_paginated_response(response)
        except Exception as e:
            response = {
                "message": 'Error something went wrong', "status": 'error'}
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({})
