from brownie import Bank
from .helper import get_account, get_profile


def create_account(name):
	print('Creating account..........')
	bank = Bank[-1]
	account = get_account()
	transaction = bank.create_account(name, {"from": account})
	transaction.wait(1)
	print('Account created successfully')
	print('Retrieving profile..........')
	profile = get_profile(bank.get_profile())
	print(profile._asdict())

	# txn = bank.deposit({"from": account, "value": Web3.toWei(0.1, 'ether')})
	# txn.wait(1)
	# profile = list(bank.get_profile())
	# profile[2] = float(Web3.fromWei(profile[2], 'ether'))


def main():
	create_account('Louis Ohaegbu')
