from collections import namedtuple
from web3 import Web3

from brownie import network, accounts, config, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
FORKED_BLOCKCHAIN_ENVIRONMENTS = ['mainnet_fork_dev']

def get_account():
	if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or \
			network.show_active() in FORKED_BLOCKCHAIN_ENVIRONMENTS:
		return accounts[0]
	else:
		return accounts.add(config['wallets']['from_key'])


def get_mock():
	if len(MockV3Aggregator) <= 0:
		mock = MockV3Aggregator.deploy({"from": get_account()})
	else:
		mock = MockV3Aggregator[-1]
	return mock.address


def get_profile(profile: tuple):
	profile_ = namedtuple('Profile', 'name address balance')
	profile = list(profile)
	profile[2] = f"{float(Web3.fromWei(int(profile[2]), 'ether'))} eth"
	profile = profile_(*profile)
	return profile
