from django.shortcuts import render
from .models import Borrower, Loan


# Create your views here.
def index(request):
    borrower_close = Loan.objects.all().filter(status='2')
    borrower_in_2022 = Loan.objects.filter(created_at__year=2022)
    all_amount_in_2021 = Loan.objects.filter(created_at__year=2021, status='1')
    sum_amount_2021 = 0
    for x in all_amount_in_2021:
        sum_amount_2021 += x.amount

    return render(request, './index.html', {'borrower_close': borrower_close,
                                            'amount_closed': len(borrower_close),
                                            'borrower_in_2022': borrower_in_2022,
                                            'amount_borrower_in_2022': len(borrower_in_2022),
                                            'sum_amount_2021': sum_amount_2021})
