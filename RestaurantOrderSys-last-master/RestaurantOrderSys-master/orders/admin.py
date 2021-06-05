from django.contrib import admin
from django.contrib import admin
from .models import Category, RegularPizza, SicilianPizza, Toppings, Hawka, Pasta, Salad, UserOrder, SavedCarts,Profile
from tinymce.widgets import TinyMCE
from django.db import models

class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class SicilianPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

admin.site.register(Profile)

admin.site.register(Category,CategoryAdmin)
admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Hawka)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
