from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Salary:
    currency: str | None = None
    salary_from: int | None = None
    salary_to: int | None = None

    def __salary_type_content(self, content):
        for s, t in zip(self.salary, content):
            if not (type(s) == type(t)):
                return False
        return True

    def __eq__(self, other):
        assert isinstance(other, Salary)

        if not self.salary_from and not self.salary_to and not other.salary_from and not other.salary_to:
            return True

        elif not self.salary_from and self.salary_to and not other.salary_from and other.salary_to:
            return self.salary_to == other.salary_to

        elif self.salary_from and not self.salary_to and other.salary_from and not other.salary_to:
            return self.salary_from == other.salary_from

        elif self.salary_from and self.salary_to and other.salary_from and other.salary_to:
            return (self.salary_from == other.salary_from) and (self.salary_to == other.salary_to)

        elif self.salary_from and not self.salary_to and other.salary_from and other.salary_to:
            return self.salary_from == other.salary_from

        elif not self.salary_from and self.salary_to and other.salary_from and other.salary_to:
            return self.salary_to == other.salary_to

        elif self.salary_from and self.salary_to and other.salary_from and not other.salary_to:
            return self.salary_from == other.salary_from

        elif self.salary_from and self.salary_to and not other.salary_from and other.salary_to:
            return self.salary_to == other.salary_to

    def __ne__(self, other):
        assert isinstance(other, Salary)

        self.salary = [self.salary_from, self.salary_to, other.salary_from, other.salary_to]

        if self.salary.count(None) == 3:
            return True
        elif ((self.__salary_type_content([None, None, 1, None]) or
              self.__salary_type_content([None, None, None, 1]) or
              self.__salary_type_content([None, None, 1, 1])) or
              self.__salary_type_content([1, None, None, None]) or
              self.__salary_type_content([None, 1, None, None]) or
              self.__salary_type_content([1, 1, None, None]) or
              self.__salary_type_content([1, None, None, 1]) or
              self.__salary_type_content([None, 1, 1, None])):
            return True
        else:
            return not self.__eq__(other)

    def __lt__(self, other):
        assert isinstance(other, Salary)

        self.salary = [self.salary_from, self.salary_to, other.salary_from, other.salary_to]

        if self.salary.count(None) == 4:
            return False

        elif not self.salary_from and not self.salary_to:
            return True

        elif self.__salary_type_content([1, None, 1, None]):
            return self.salary_from < other.salary_from

        elif self.__salary_type_content([1, 1, 1, None]):
            return self.salary_from < other.salary_from

        elif self.__salary_type_content([1, None, 1, 1]):
            return self.salary_from < other.salary_from

        elif self.__salary_type_content([None, 1, None, 1]):
            return self.salary_to < other.salary_to

        elif self.__salary_type_content([None, 1, 1, 1]):
            return self.salary_to < other.salary_to

        elif self.__salary_type_content([1, 1, None, 1]):
            return self.salary_to < other.salary_to

        elif self.__salary_type_content([1, 1, 1, 1]):
            return ((self.salary_from + self.salary_to) / 2) < ((other.salary_from + other.salary_to) / 2)

    def __gt__(self, other):
        assert isinstance(other, Salary)

        self.salary = [self.salary_from, self.salary_to, other.salary_from, other.salary_to]

        if self.salary.count(None) == 4:
            return False

        elif not other.salary_from and not other.salary_to:
            return True

        elif self.__salary_type_content([1, None, 1, None]):
            return self.salary_from > other.salary_from

        elif self.__salary_type_content([1, 1, 1, None]):
            return self.salary_from > other.salary_from

        elif self.__salary_type_content([1, None, 1, 1]):
            return self.salary_from > other.salary_from

        elif self.__salary_type_content([None, 1, None, 1]):
            return self.salary_to > other.salary_to

        elif self.__salary_type_content([None, 1, 1, 1]):
            return self.salary_to > other.salary_to

        elif self.__salary_type_content([1, 1, None, 1]):
            return self.salary_to > other.salary_to

        elif self.__salary_type_content([1, 1, 1, 1]):
            return ((self.salary_from + self.salary_to) / 2) > ((other.salary_from + other.salary_to) / 2)

    def __le__(self, other):
        if self.__lt__(other) or self.__eq__(other):
            return True
        return False

    def __ge__(self, other):
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False


@dataclass(unsafe_hash=True)
class Vacancy:
    name: str
    url: str
    employer_name: str
    salary: Salary
