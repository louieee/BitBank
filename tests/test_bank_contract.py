from collections import namedtuple

import pytest
from brownie import accounts, Bank, exceptions
from web3 import Web3


def get_suite():
	suite = namedtuple("Suite", 'account sender bank')
	suite.account = accounts[0]
	suite.sender = {"from": suite.account}
	suite.bank = Bank.deploy(suite.sender) if len(Bank) <= 0 else Bank[-1]
	return suite


def test_account_created():
	from scripts.create_account import create_account
	suite = get_suite()
	create_account('louis')
	profile = suite.bank.get_profile()
	assert profile[0] == 'louis'
	assert profile[2] == 0
	assert profile[1] is not None


def test_account_created_twice():
	from scripts.create_account import create_account
	with pytest.raises(exceptions.VirtualMachineError):
		create_account('louis')


def test_deposit():
	from scripts.deposit import deposit
	suite = get_suite()
	profile = suite.bank.get_profile()
	amount = 0.05
	previous_bal = float(Web3.fromWei(profile[2], 'ether'))
	deposit(amount)
	profile = suite.bank.get_profile()
	new_balance = float(Web3.fromWei(profile[2], 'ether'))
	difference = new_balance - previous_bal
	assert difference >= amount


def test_withdraw():
	from scripts.withdraw import withdraw
	suite = get_suite()
	profile = suite.bank.get_profile()
	amount = 0.02
	previous_bal = float(Web3.fromWei(profile[2], 'ether'))
	withdraw(amount)
	profile = suite.bank.get_profile()
	new_balance = float(Web3.fromWei(profile[2], 'ether'))
	difference = previous_bal - new_balance
	assert difference >= amount


def test_withdraw_more_than_bal():
	from scripts.withdraw import withdraw
	amount = 1
	with pytest.raises(exceptions.VirtualMachineError):
		withdraw(amount)
