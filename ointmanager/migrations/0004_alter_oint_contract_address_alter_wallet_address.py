# Generated by Django 5.0.6 on 2024-06-30 15:29

import django.core.validators
import eth_utils.address
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ointmanager', '0003_oint_abi_string_alter_oint_contract_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oint',
            name='contract_address',
            field=models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$'), eth_utils.address.is_checksum_address], verbose_name='Oint Contract Address'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='address',
            field=models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$'), eth_utils.address.is_checksum_address], verbose_name='Wallet Address'),
        ),
    ]
