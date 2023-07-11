import django_filters
from .models import *


class PatientFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter()

    class Meta:
        model = Patient
        fields = {
            'created_at': ['date__gte', 'date__lte'],
        }


class VisitFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    date = django_filters.DateFilter(
        field_name="date")
    bmi_gt = django_filters.DateFilter(
        field_name="bmi", lookup_expr='gt')
    bmi_lt = django_filters.DateFilter(
        field_name="bmi", lookup_expr='lt')

    class Meta:
        model = Visit
        fields = {
            'bmi': ['gte', 'lte'],
            'created_at': ['date__gte', 'date__lte'],
        }
