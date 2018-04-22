from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from . import models

from account import models as account_model


@task
def mul(x, y):
    total = x * (y * random.randint(3, 100))

    deploy = models.Mul(total=total)
    deploy.save()

    return total

@task(name='change_membership_status')
def membership_change(user_id, payment_id):
    user_obj = account_model.UserProfile.objects.get(id=user_id)
    free_membership_obj = account_model.Membershiplevel.objects.get(name='free')
    user_obj.membership = free_membership_obj
    user_obj.payments = None
    user_obj.save()

    payment = account_model.Payment.objects.get(id=payment_id)
    payment.is_verify = 'expired'
    payment.save()



#tomorrow = datetime.utcnow() + relativedelta(months=6)
#today = datetime.utcnow() + relativedelta(seconds=20)

#mul.apply_async(args=[2, 3], eta=tomorrow)
#mul.apply_async(args=[2, 3], eta=today)
