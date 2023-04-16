from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='car_brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='car_brand', lookup_expr='iendswith')
    brand_contain = filters.CharFilter(field_name='car_brand', lookup_expr='icontains')
