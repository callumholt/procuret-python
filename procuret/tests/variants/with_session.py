"""
Procuret Python
Test With Session Module
author: hugh@blinkybeach.com
"""
from procuret.tests.test import Test
from procuret.session import Session, Perspective
from typing import Optional
from procuret.security.second_factor_code import SecondFactorCode


class TestWithSession(Test):

    test_perspective: Perspective = NotImplemented

    _tws_cached_session: Optional[Session] = None

    session = property(lambda s: s._tws_load_session())

    def _tws_load_session(self) -> Session:

        if self._tws_cached_session is None:

            if not isinstance(self.test_perspective, Perspective):
                raise NotImplementedError('Implement .test_perspective')

            SecondFactorCode.create_with_email(
                email=self.email,
                plaintext_secret=self.secret,
                perspective=self.test_perspective
            )

            code = input('Second factor code: ')

            if not code.isdigit():
                raise ValueError('Second factor code must be integer')
            
            if not len(code) == 6:
                raise ValueError('Second factor code must be six digits')

            self._tws_cached_session = Session.create_with_email(
                email=self.email,
                code=code,
                plaintext_secret=self.secret,
                perspective=self.test_perspective
            )
        return self._tws_cached_session
