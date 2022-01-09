from typing import Any
from boa3.builtin.interop.storage import delete, get, put
from boa3.builtin.type import UInt160

data = {
    'tx_1':
        {  # deposit 100 bNEO -> mint 100 sNEO
            'bNEO': 100,
            'sNEO': 100,
            'ratio': 1,  # 1 sNEO == 1 bNEO
        },
    'compound_event_1':
        {  # earned 1 bNEO
            'bNEO': 101,
            'sNEO': 100,
            'ratio': 1.01,  # 1 sNEO = 1.01 bNEO
        },
    'tx_2':
        {  # deposit 100 bNEO -> mint 99 sNEO
            'bNEO': 201,
            'sNEO': 199,
            'ratio': 1.01,  # 1 sNEO = 1.01 bNEO
        },
    'compound_event_2':
        {  # earned 2 bNEO
            'bNEO': 203,
            'sNEO': 199,
            'ratio': 1.02,  # 1 sNEO = 1.02 bNEO
        },
    'tx_3':
        {  # withdraw 100 sNEO -> 102 bNEO
            'bNEO': 101,
            'sNEO': 99,
            'ratio': 1.02,  # 1 sNEO = 1.02 bNEO
        },
    'compound_event_3':
        {  # earned 2 bNEO
            'bNEO': 103,
            'sNEO': 99,
            'ratio': 1.04,  # 1 sNEO = 1.04 bNEO
        },
}

OWNER = UInt160()


class SandwichNeo:
    """
    Pseudo class for sandwich neo smart contract
    """

    def __init__(self):
        self.owner = OWNER
        self.total_supply = 0
        self.symbol = 'sNEO'
        self.decimals = 8

        self.storage = {}

    def symbol(self):
        return self.symbol

    def decimals(self):
        return self.decimals

    def totalSupply(self):
        return self.total_supply

    def balanceOf(self, account: UInt160):
        return self.storage[account]

    def transfer(self, from_address: UInt160, to_address: UInt160, amount: int, data: Any):
        # assert len(from_address) == 20 and len(to_address) == 20
        # assert amount >= 0
        #
        # # The function MUST return false if the from account balance does not have enough tokens to spend.
        # from_balance = get(from_address).to_int()
        # if from_balance < amount:
        #     return False
        #
        # # The function should check whether the from address equals the caller contract hash.
        # # If so, the transfer should be processed;
        # # If not, the function should use the check_witness to verify the transfer.
        # if from_address != calling_script_hash:
        #     if not check_witness(from_address):
        #         return False
        #
        # # skip balance changes if transferring to yourself or transferring 0 cryptocurrency
        # if from_address != to_address and amount != 0:
        #     if from_balance == amount:
        #         delete(from_address)
        #     else:
        #         put(from_address, from_balance - amount)
        #
        #     to_balance = get(to_address).to_int()
        #     put(to_address, to_balance + amount)
        #
        # # if the method succeeds, it must fire the transfer event
        # on_transfer(from_address, to_address, amount)
        # # if the to_address is a smart contract, it must call the contracts onPayment
        # post_transfer(from_address, to_address, amount, data, True)
        # # and then it must return true
        return True

    # todo - continue
