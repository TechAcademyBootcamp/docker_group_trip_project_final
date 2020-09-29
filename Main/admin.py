from django.contrib import admin
from Main.models import Contact,City,Places,Helps,ContactInfo,StaticPage,AboutProject,WebsiteSettings, \
    Subscriber,CityImages

admin.site.register(Contact)
# admin.site.register(City)
admin.site.register(Places)
admin.site.register(Helps)
admin.site.register(ContactInfo)
admin.site.register(StaticPage)
admin.site.register(AboutProject)
admin.site.register(WebsiteSettings)
admin.site.register(Subscriber)

class CityImageInline(admin.TabularInline):
    model = CityImages
    extra = 3

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [ CityImageInline, ]