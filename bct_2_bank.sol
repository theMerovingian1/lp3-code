// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Bank {
    mapping (address => uint) private balances;

    event Deposit (address indexed accountHolder, uint amount);

    event Withdraw(address indexed accountHolder, uint amount);

    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        balances[msg.sender] += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");

        require(balances[msg.sender] >= _amount, "Insufficient funds");

        balances[msg.sender] -= _amount;
        payable(msg.sender).transfer(_amount);

        emit Withdraw(msg.sender, _amount);
    }

    function getBalance() external view returns (uint) {
        return balances[msg.sender];
    }
}