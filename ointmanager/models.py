from django.db import models
from django.core.validators import RegexValidator

import uuid
from web3 import Web3

#TODO add basescan validator

# models for users, companies, wallets, and oint contracts
class Wallet(models.Model):
    '''
    Wallet information
    '''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4) 
    type = models.CharField(
        max_length=40,
        choices = {
            'USR':'User',
            'CMP':'Company'
        }
    )
    address = models.CharField(
        verbose_name="Wallet Address",
        max_length=42,
        unique=True,
        validators=[RegexValidator(regex=r'^0x[a-fA-F0-9]{40}$'), Web3.is_checksum_address],
    )

class User(models.Model):
    '''
    User information. Oints sent to this user_id will go to this wallet_address
    '''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4)
    name = models.CharField(max_length=200)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

class Company(models.Model):
    '''
    Company information
    '''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4) 
    name = models.CharField(max_length=200)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    api_key = models.UUIDField(
         default = uuid.uuid4) 

class Oint(models.Model):
    '''
    Oint information. Oints are just ERC-20 tokens that can be redeemed
    '''
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract_address = models.CharField(
        verbose_name="Oint Contract Address",
        max_length=42,
        unique=True,
        validators=[RegexValidator(regex=r'^0x[a-fA-F0-9]{40}$'), Web3.is_checksum_address],
    )
    abi_string = models.CharField(
        verbose_name="Oint ABI string",
        max_length=20000,
    )
