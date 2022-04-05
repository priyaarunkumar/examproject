from django.contrib import admin
from . models import Place
from . models import Country
from . models import Person
from . models import City
from . models import Food
from . models import Prize
from . models import Quantity
# Register your models here.
admin.site.register(Place)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Food)
admin.site.register(Prize)
admin.site.register(Quantity)