from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    login: str
    password: str


@dataclass(frozen=True)
class VerificationCode:
    code: str


class Helper:

    @staticmethod
    def get_user():
        return User('vasya', 'qwerty123')

    @staticmethod
    def get_verification_code():
        return VerificationCode('12345')