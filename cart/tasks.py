import dramatiq

from .email import Email
from .warehouse import Warehouse


@dramatiq.actor
def prepare_skus(skus):
    Warehouse.prepare(*skus)


@dramatiq.actor
def congratulate_user():
    Email.congratulate_on_purchase()
