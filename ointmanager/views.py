from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from ointmanager.models import Oint, User

import requests
from dotenv import dotenv_values
from web3 import Web3, AsyncWeb3

###

w3 = Web3(Web3.HTTPProvider(f"https://base-sepolia.g.alchemy.com/v2/{dotenv_values('.env')['ALCHEMY_API_KEY']}"))

###

def index(request):
    return HttpResponse("Welcome to Oints.")

###apis

#checkbalance

def checkbalance(oint_id, address):
    oint = get_object_or_404(Oint, pk=oint_id)
    token = w3.eth.contract(address=oint.contract_address, abi=oint.abi) # declaring the token contract
    token_balance = token.functions.balanceOf(address).call() # returns int with balance, without decimals
    return JsonResponse({"oint_id":oint_id, "holder_address":address, "token_balance":token_balance})

#mint oints

def mint_oints_to_user(oint_id, user_id, company_api_key):
    user = get_object_or_404(User, pk=user_id)
    return mint_oints_to_address(oint_id, user.wallet.address, company_api_key)

def mint_oints_to_address(oint_id, address, company_api_key):
    oint = get_object_or_404(Oint, pk=oint_id)
    assert oint.company.api_key == company_api_key

    # Initialize the address calling the functions/signing transactions
    caller = dotenv_values(".env")['WALLET_ADDRESS']
    private_key = dotenv_values(".env")['WALLET_KEY']  # To sign the transaction
    nonce = w3.eth.get_transaction_count(caller)
    # Create smart contract instance
    contract = w3.eth.contract(address=oint.contract_address, abi=oint.abi_string)
    # call function, sign, and send transaction
    Chain_id = w3.eth.chain_id
    call_function = contract.functions.mint(address).buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce})
    signed_tx = w3.eth.account.sign_transaction(call_function, private_key=private_key)
    sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(sent_tx)

    return JsonResponse(tx_receipt)

#use oints