"""
Procuret Python
Test With Supplier Module
author: hugh@blinkybeach.com
"""
from procuret.ancillary.command_line import CommandLine
from procuret.tests.test import Test


class TestWithSupplier(Test):

    def __init__(self) -> None:

        cl = CommandLine.load()

        self._supplier_id = cl.require(
            key='--supplier-id',
            of_type=int,
            type_name='integer'
        )

        return super().__init__()

    supplier_id = property(lambda s: s._supplier_id)
