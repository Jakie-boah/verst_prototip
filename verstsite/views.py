from django.shortcuts import render
from handler.models import *
from items.filter import ListingFilter
from items.models import TestItemModel
from cities.models import City
from location.models import Locations
from contacts.models import *
from contacts_sales.models import SalesContacts


def index(request):
    header_contact = HeaderContacts.objects.all().first()
    items = TestItemModel.objects.all()
    cities = City.objects.all()
    item_filter = ListingFilter(request.GET, queryset=items)
    params = {
        'header_contact': header_contact,
        'item_filter': item_filter,
        'cities': cities
    }
    return render(request, './index.html', params)


def register(request):
    return render(request, './register.html')


def log_in(request):
    return render(request, './login.html')


def check(request):
    return render(request, './check_order.html')


def reviews(request):
    return render(request, './reviews.html')


def vacancy(request):
    vacancy_contacts = VacancyContacts.objects.all().first()
    return render(request, './vacancy.html', {'vacancy_contacts': vacancy_contacts})


def contacts(request):
    moscow_contacts = MoscowContacts.objects.all().first()
    peter_contacts = PeterContacts.objects.all().first()
    voronezh_contacts = VoronezhContacts.objects.all().first()
    rest_contacts = RestOfContacts.objects.all().first()

    params = {
        'moscow_contacts': moscow_contacts,
        'peter_contacts': peter_contacts,
        'voronezh_contacts': voronezh_contacts,
        'rest_contacts': rest_contacts
    }

    return render(request, './contacts.html', params)


def sales(request):
    sales_contacts = SalesContacts.objects.all().first()
    return render(request, './sales.html', {'sales_contacts': sales_contacts})


def buy(request, item_id):
    locations = Locations.objects.filter(item__id__exact=item_id).all()
    return render(request, './buy.html', {'locations': locations})


def choose(request):
    return render(request, './choose.html')


def choose1(request):
    return render(request, './choose1.html')


def end(request):
    return render(request, './end.html')


def add(request):
    return render(request, './add.html')


def tech_work(request):
    return render(request, './techwork.html')
