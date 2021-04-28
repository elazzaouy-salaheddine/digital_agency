from django.contrib import admin
from.models import portfolio_item, category
# Register your models here.


admin.site.register(category)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title','client','category','project_date']
    list_filter = ['category']
admin.site.register(portfolio_item,PortfolioAdmin)