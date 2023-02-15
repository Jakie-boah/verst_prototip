from django import forms
from .models import TestItemModel
from cities.models import City
from django.forms import SelectMultiple
import django_filters


class ListingFilter(django_filters.FilterSet):
    city = django_filters.ModelMultipleChoiceFilter(lookup_expr='exact', queryset=City.objects.all(), widget=SelectMultiple())

    class Meta:
        model = TestItemModel
        fields = {'city': ['exact']}

    def __init__(self, *args, **kwargs):
        super(ListingFilter, self).__init__(*args, **kwargs)
        self.form.initial['city'] = 1
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['city'] = City.objects.all()
    #     context['filter'] = ListingFilter(self.request.GET, queryset=TestItemModel.objects.all())
    #     return context
