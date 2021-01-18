"""
Procuret Python
Test With Supplier Module
author: hugh@blinkybeach.com
"""
from procuret.ancillary.command_line import CommandLine
from procuret.tests.variants.with_session import TestWithSession


class TestWithSupplier(TestWithSession):

    def __init__(self) -> None:

        cl = CommandLine.load()

        self._supplier_id = cl.require(
            key='--supplier-id',
            of_type=int,
            type_name='integer'
        )

        return super().__init__()

    supplier_id = property(lambda s: s._supplier_id)

    # _tws_cached_supplier: Optional[Supplier] = None

    # def _tws_load_supplier(self) -> Supplier:

    #    if self._tws_cached_supplier is None:
    #        raise NotImplementedError

    #    return self._tws_cached_supplier
