from brownie import config, network, Bank
from .helper import get_account, get_mock


def deploy_contract():
	account = get_account()
	print(network.show_active(), "-----------> network")
	print(account, "--------------> Account")
	if network.show_active() not in ['development', 'ganache-local']:
		price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
	else:
		'''
		The mock solidity file will be deployed here and the address passed as the
		price feed address
		'''
		price_feed_address = get_mock()
	'''
	assuming we were passing the constructor field to the contract from different networks
	bank = Bank.deploy(price_feed_address, {"from": account}, publish_source=True)
	'''
	print("Deploying the bank contract.............")
	bank = Bank.deploy({"from": account}, publish_source=config['networks'][network.show_active()]['verify'])
	print("Finished deploying bank contract........")
	print(bank)


def main():
	deploy_contract()
