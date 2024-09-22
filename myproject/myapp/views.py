

from django.shortcuts import render
from .signals import send_signal_within_transaction

def test_view(request):
    send_signal_within_transaction()
    return render(request, 'myapp/test.html', {})

