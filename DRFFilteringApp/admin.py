from django.contrib import admin
from .models import WFMTModel
# Register your models here.
@admin.register(WFMTModel)
class WFMTMOdelAdmin(admin.ModelAdmin):
    list_display = ('id','cp_number','sne_id','scheme_number','trs')
    