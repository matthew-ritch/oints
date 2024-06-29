// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";

/**
 * @title Generic Oint Token
 * @notice Oint Tokens are ERC20 tokens deployed on BASE mainnet, using OpenZeppelin libraries. 
 */

contract OintToken is ERC20, ERC20Burnable, Ownable, ERC20Permit {

    constructor(string memory _ointName, string memory _symbol, address owner)
        ERC20(_ointName, _symbol)
        ERC20Permit(_ointName)
        Ownable(owner)
    {}

    /**
     * @notice Mints new oints and distributes them to the specified address
     * @param to The address to which the minted oints will be distributed
     * @param amount The amount of the oints to mint and distribute to the `to` address
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
        if (amount <= 100) {
            _mint(owner(), 1);
        }
        if (amount > 100) {
            _mint(owner(), amount / 100);
        }
    }
}

contract OintFactory {
    function CreateOint(string memory _ointName, string memory _symbol) public returns (address) {
        OintToken newOint = new OintToken(_ointName, _symbol, msg.sender);
        return address(newOint);
    }
}