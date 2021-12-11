import pytest
from boa3_test.tests.boa_test import BoaTest
from boa3_test.tests.test_classes.testengine import TestEngine
from .consts import NEO_CONTRACTS_DIR_PATH


class BaseTest(BoaTest):
    """
    Base Test for testing smart contracts
    """

    @pytest.fixture(scope='class', autouse=True)
    def setup_class(self, contract):
        cls = type(self)
        cls.contract_path = self.get_contract_path(NEO_CONTRACTS_DIR_PATH, contract)

    # @pytest.fixture(autouse=True)
    # def setup(self):
    #     self.engine = TestEngine()
    #
    # def invoke(self, method: str):
    #     """
    #     Invokes contract method
    #     :param method: The contract method name
    #     :return: The returned value from contract.
    #     """
    #     return self.engine.run(self.compiled_contract_path, method)
