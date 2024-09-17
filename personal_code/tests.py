from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Entering_personal_code, dict(mother_code="AA", father_code="BB", city_code="CC", birthday_code="000", code="AABBCC000")
        yield Start_T2