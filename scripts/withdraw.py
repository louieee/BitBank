from brownie import Bank
from .helper import get_account, get_profile
from web3 import Web3


def withdraw(amount: float, address=None):
	account = get_account() if address is None else address
	print(f'Withdraw {amount} eth into account {account}...........')
	bank = Bank[-1]
	account = get_account()
	if address:
		transaction = bank.transfer(address, Web3.toWei(amount, "ether"), {"from": account})
	else:
		transaction = bank.withdraw(Web3.toWei(amount, "ether"), {"from": account})
	transaction.wait(1)
	print('Withdrawal is successful......')
	print('Retrieving profile..........')
	profile = get_profile(bank.get_profile())
	print(profile._asdict())


def main():
	withdraw(0.1)
