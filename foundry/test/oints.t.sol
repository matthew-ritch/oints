// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {OintToken} from "../src/oints.sol";

contract OintTokenTest is Test {
    OintToken public oint;

    function setUp() public {
        oint = new OintToken('testoint','toint');
    }

}
