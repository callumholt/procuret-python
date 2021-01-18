"""
Procuret Python
Test With Session Module
author: hugh@blinkybeach.com
"""
from procuret.tests.test import Test
from procuret.session import Session, Perspective
from typing import Optional


class TestWithSession(Test):

    test_perspective: Perspective = NotImplemented

    _tws_cached_session: Optional[Session] = None

    session = property(lambda s: s._tws_load_session())

    def _tws_load_session(self) -> Session:

        if self._tws_cached_session is None:

            if not isinstance(self.test_perspective, Perspective):
                raise NotImplementedError('Implement .test_perspective')

            self._tws_cached_session = Session.create_with_email(
                email=self.email,
                plaintext_secret=self.secret,
                perspective=self.test_perspective
            )
        return self._tws_cached_session
