# Generated by Django 2.2.5 on 2021-02-06 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttransaction',
            old_name='xpayaccount_email',
            new_name='xpayaccount',
        ),
    ]
