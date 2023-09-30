from celery import shared_task
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    print('----order_created task----')
    try:
        order = Order.objects.get(id=order_id)
        subject = f'Order nr. {order.id}'
        message = f'Dear {order.first_name},\n\n' \
                  f'You have successfully placed an order.' \
                  f'Your order ID is {order.id}.'
        mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
        return mail_sent
    except ObjectDoesNotExist:
        # Handle the case where the order does not exist
        # Log the error or perform appropriate actions
        return None
    except Exception as e:
        # Handle other exceptions that might occur during the task
        # Log the error or perform appropriate actions
        return None
