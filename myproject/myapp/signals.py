import time
import threading
from django.dispatch import Signal, receiver
from django.db import transaction
from myapp.models import MyModel

# Define a custom signal
my_signal = Signal()

# Signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler started in thread: {threading.current_thread().name}")
    time.sleep(5)  # Simulating a time-consuming operation
    MyModel.objects.create(name="Created in signal")
    print("Signal handler completed")

# Function to trigger the signal within a transaction
def send_signal_within_transaction():
    with transaction.atomic():
        print("Inside transaction, before signal")
        MyModel.objects.create(name="Initial object")
        my_signal.send(sender=None)
        print("Inside transaction, after signal")
