from django.contrib import admin
from .models import Borrower, Loan


# Register your models here.
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_display_links = ('name',)
    fields = ('name',)


class LoanAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'status', 'created_at', 'amount',)
    list_display_links = ('borrower', 'status', 'amount',)
    fields = ('borrower', 'status', 'amount',)


admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Loan, LoanAdmin)
