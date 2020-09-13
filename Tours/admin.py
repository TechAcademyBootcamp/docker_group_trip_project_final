from django.contrib import admin
from Tours.models import Tours, TourImages , TourComments

# admin.site.register(Tours)
admin.site.register(TourComments)
admin.site.register(TourImages)

class TourImageInline(admin.TabularInline):
    model = TourImages
    extra = 3

@admin.register(Tours)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ TourImageInline, ]

