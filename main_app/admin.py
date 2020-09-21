from django.contrib import admin
from .models import customerTestimony, fourImageGallary, set_frequently_asked_question
# Register your models here.
admin.site.site_header = 'Sprucified Laundries Admin Dashboard'

admin.site.register(customerTestimony)
admin.site.register(set_frequently_asked_question)
admin.site.register(fourImageGallary)
