from django_filters import rest_framework as filters


class AutoParkFilter(filters.FilterSet):
    year_lt = filters.NumberFilter(field_name='cars__year', lookup_expr='lt', distinct=True)

