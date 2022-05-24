// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Account {
    address owner;
    string name;

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

    constructor() public payable{
        owner = msg.sender;
    }


    modifier owner_only{
        require(msg.sender == owner, "You do not have permission to do this!");
        _;
    }

    function set_name (string memory name_) public owner_only {
        name = name_;
    }

    function transfer(address payable identifier, uint amount) public payable owner_only {
        require (address(this).balance > amount, "Insufficient balance!");
        identifier.transfer(amount);
        transactions_count ++;
        transfer_txns_count ++;
        Transaction memory transfer_txn = Transaction(transactions_count, address(this), identifier, "transfer", amount);
        transactions[transactions_count] = transfer_txn;
        transfer_txns[transactions_count] = transfer_txn;
    }
    function withdraw(uint amount) public owner_only {
        require (address(this).balance > amount, "Insufficient balance!");
        msg.sender.transfer(amount);
        transactions_count ++;
        withdrawal_txns_count ++;
        Transaction memory withdraw_txn = Transaction(transactions_count, address(this), address(0), "withdraw", amount);
        transactions[transactions_count] = withdraw_txn;
        withdrawal_txns[transactions_count] = withdraw_txn;
    }

    function deposit() public payable{
        transactions_count ++;
        deposit_txns_count ++;
        Transaction memory deposit_txn = Transaction(transactions_count, msg.sender, address(this), "deposit", msg.value);
        transactions[transactions_count] = deposit_txn;
        deposit_txns[transactions_count] = deposit_txn;
    }
    function get_profile() public view returns(string memory username, address owner_address,  address account, uint balance){
        username = name;
        owner_address = owner;
        account = address(this);
        balance = account.balance;
    }

}


