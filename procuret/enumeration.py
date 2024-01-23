class PR_Enumeration:

    @staticmethod
    def enumerations():
        raise NotImplementedError("Not implemented")

    def __init__(self, indexid, name):
        self._indexid = indexid
        self._name = name

    @property
    def indexid(self):
        return self._indexid

    @property
    def name(self):
        return self._name

    def equal_to(self, other):
        if other is None:
            return False
        return other.indexid == self._indexid

    def not_equal_to(self, other):
        return not self.equal_to(other)

    def is_in(self, others):
        if not others:
            return False
        return any(self.equal_to(other) for other in others)

    def is_not_in(self, others):
        return not self.is_in(others)

    @staticmethod
    def with_id(indexid, type_):
        for candidate in type_.enumerations():
            if candidate.indexid == indexid:
                return candidate
        raise ValueError(
            f'Unknown indexid {indexid} for type enum {type_.__name__}')

    @staticmethod
    def decode(data, type_):
        return PR_Enumeration.with_id(data, type_)

    @staticmethod
    def optionally_decode(data, type_):
        if not data or data == 'null':
            return None
        return PR_Enumeration.decode(data, type_)
