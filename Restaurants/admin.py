from django.contrib import admin
from Restaurants.models import RestaurantImages, Restaurants,ToEatReason, OptionListTypeCheckbox,\
    OptionListTypeRadio, OptionsTypeCheckbox, OptionsTypeRadio

admin.site.register(OptionListTypeCheckbox)
admin.site.register(OptionListTypeRadio)
admin.site.register(OptionsTypeCheckbox)
admin.site.register(OptionsTypeRadio)
admin.site.register(RestaurantImages)
# admin.site.register(Restaurants)
admin.site.register(ToEatReason)

class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImages
    extra = 3

@admin.register(Restaurants)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ RestaurantImageInline, ]

# Register your models here.
