from brownie import Bank
from .helper import get_account, get_profile
from web3 import Web3


def deposit(amount: float, bank=None):
	print(f'Depositing {amount} eth into account...........')
	bank = Bank[-1] if bank is None else bank
	account = get_account()
	transaction = bank.deposit({"from": account, "value": Web3.toWei(amount, 'ether')})
	transaction.wait(1)
	print('Deposit is successful......')
	print('Retrieving profile..........')
	profile = get_profile(bank.get_profile())
	print(profile._asdict())


def main():
	deposit(0.2)