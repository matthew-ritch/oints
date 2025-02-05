# Generated by Django 5.0.6 on 2024-06-30 15:31

import django.core.validators
import eth_utils.address
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ointmanager', '0005_alter_oint_contract_address_alter_wallet_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='api_key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='oint',
            name='contract_address',
            field=models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$'), eth_utils.address.is_checksum_address], verbose_name='Oint Contract Address'),
        ),
        migrations.AlterField(
            model_name='oint',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='address',
            field=models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$'), eth_utils.address.is_checksum_address], verbose_name='Wallet Address'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
