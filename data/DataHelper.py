import random
from dataclasses import dataclass


def get_valid_amount(balance):
    return random.randint(1, balance)


@dataclass(frozen=True)
class User:
    login: str
    password: str


@dataclass(frozen=True)
class VerificationCode:
    code: str


@dataclass(frozen=True)
class Card:
    number: str
    test_id: str


class Helper:

    @staticmethod
    def get_user():
        return User('vasya', 'qwerty123')

    @staticmethod
    def get_verification_code():
        return VerificationCode('12345')

    @staticmethod
    def get_cards():
        return [Card("5559 0000 0000 0001", "92df3f1c-a033-48e6-8390-206f6b1f56c0"),
                Card("5559 0000 0000 0002", "0f3f5c2a-249e-4c3d-8287-09f7a039391d")]
