from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        if (self.player.participant.PGG_first and self.player.round_number == 1) or (not self.player.participant.PGG_first and self.player.round_number == 2):
            yield Transition_to_PGG
            yield PGG_instructions
            yield PGG_transition_to_comprehension_check
            yield PGG_comprehension_check, dict(PGG_comprehension1=600, PGG_comprehension2=0)
        if (not self.player.participant.PGG_first and self.player.round_number == 1) or (self.player.participant.PGG_first and self.player.round_number == 2):
            yield Transition_to_SVO
            yield SVO_items, dict(svo_choice_1=1, svo_choice_2=2, svo_choice_3=3, svo_choice_4=4, svo_choice_5=5, svo_choice_6=6, svo_choice_7=7, svo_choice_8=8, svo_choice_9=9, svo_choice_10=10, svo_choice_11=11, svo_choice_12=12, svo_choice_13=13, svo_choice_14=14, svo_choice_15=15)
