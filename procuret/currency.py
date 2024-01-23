from enumeration import PR_Enumeration


class PR_Currency(PR_Enumeration):
    _CURRENCY_AUD = None
    _CURRENCY_NZD = None

    @staticmethod
    def enumerations():
        return [PR_Currency._CURRENCY_AUD, PR_Currency._CURRENCY_NZD]

    def __init__(self, indexid, iso_4217, name, exponent, symbol):
        super().__init__(indexid, name)
        self._iso_4217 = iso_4217.upper()
        self._exponent = exponent
        self._symbol = symbol

    @property
    def iso_4217(self):
        return self._iso_4217

    @property
    def symbol(self):
        return self._symbol

    @property
    def exponent(self):
        return self._exponent

    @staticmethod
    def AUD():
        return PR_Currency._CURRENCY_AUD

    @staticmethod
    def NZD():
        return PR_Currency._CURRENCY_NZD

    @staticmethod
    def all_available():
        return [PR_Currency._CURRENCY_AUD, PR_Currency._CURRENCY_NZD]

    @staticmethod
    def decode(data):
        return PR_Currency(data['indexid'], data['iso_4217'], data['name'],
                           data['exponent'], data['symbol'])

    @staticmethod
    def with_id(indexid):
        if indexid == PR_Currency.AUD().indexid:
            return PR_Currency.AUD()
        if indexid == PR_Currency.NZD().indexid:
            return PR_Currency.NZD()
        raise ValueError('Unknown currency ' + str(indexid))


PR_Currency._CURRENCY_AUD = PR_Currency(1, 'aud', 'Australian Dollar', 2, '$')
PR_Currency._CURRENCY_NZD = PR_Currency(2, 'nzd', 'New Zealand Dollar', 2, '$')
