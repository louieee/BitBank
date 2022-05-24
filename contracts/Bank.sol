// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Bank {

    uint accounts_count;

    mapping (address => Account) public accounts;
    mapping (address => uint) public account_address;
    mapping (address => uint) public account_owner;
    mapping (string => uint) public account_name;

    struct Account{
        uint id;
        string name;
        address owner;
        uint balance;
    }

    struct Transaction {
        uint id;
        address sender_acct;
        address receiver_acct;
        string type_;
        uint amount;
    }
    uint public transactions_count;
    uint public deposit_txns_count;
    uint public withdrawal_txns_count;
    uint public transfer_txns_count;

    mapping (uint => Transaction) public transactions;
    mapping (uint => Transaction) public deposit_txns;
    mapping (uint => Transaction) public withdrawal_txns;
    mapping (uint => Transaction) public transfer_txns;

    function transfer(address payable identifier, uint amount)public{
        require(account_address[identifier] != 0, "This account address does not exist!");
        require (accounts[msg.sender].balance > amount, "Insufficient balance!");
        identifier.transfer(amount);
        transactions_count ++;
        transfer_txns_count ++;
        Transaction memory transfer_txn = Transaction(transactions_count, msg.sender, identifier, "transfer", amount);
        transactions[transactions_count] = transfer_txn;
        transfer_txns[transactions_count] = transfer_txn;
        accounts[msg.sender].balance = accounts[msg.sender].balance - amount;
    }
    function withdraw(uint amount)public{
        require (accounts[msg.sender].balance > amount, "Insufficient balance!");
        msg.sender.transfer(amount);
        transactions_count ++;
        withdrawal_txns_count ++;
        Transaction memory withdraw_txn = Transaction(transactions_count, msg.sender, address(0), "withdraw", amount);
        transactions[transactions_count] = withdraw_txn;
        withdrawal_txns[transactions_count] = withdraw_txn;
        accounts[msg.sender].balance = accounts[msg.sender].balance - amount;
    }

    function deposit() public payable {
        transactions_count ++;
        deposit_txns_count ++;
        Transaction memory deposit_txn = Transaction(transactions_count, msg.sender, address(this), "deposit", msg.value);
        transactions[transactions_count] = deposit_txn;
        deposit_txns[transactions_count] = deposit_txn;
        accounts[msg.sender].balance = accounts[msg.sender].balance + msg.value;
    }
    function get_profile() public view returns(string memory username, address owner_address,  uint balance){
        Account memory user_account = accounts[msg.sender];
        username = user_account.name;
        owner_address = user_account.owner;
        balance = user_account.balance;
    }

    function create_account(string memory name) public {
        require(account_name[name] == 0,
        "This name has already been used by another account");
        require(account_owner[msg.sender] == 0,
        "This user already has an account!");
        accounts_count ++;
        Account memory account = Account(accounts_count, name, msg.sender, 0);
        accounts[msg.sender] = account;
        account_owner[msg.sender] = accounts_count;
        account_name[name] = accounts_count;
    }
}
