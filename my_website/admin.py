from django.contrib import admin
from my_website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display= ("name", "email", "subject", "created_date")
    list_filter = ('email' ,)
    search_fields = ['name', 'massage']
   

admin.site.register(Contact, ContactAdmin)


# Register your models here.
