from otree.api import *
from otree.api import models
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_end = models.StringField()
    code = models.StringField(label="")


# Randomisierung der SoMi-Objekte
def creating_session(subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            SoMi_objects = list(range(1, 13))
            random.shuffle(SoMi_objects)
            SoMi_objects = list(map(str, SoMi_objects))
            SoMi_objects_pre = SoMi_objects[0:4]+SoMi_objects[0:4]
            SoMi_objects_treat = SoMi_objects[4:8]+SoMi_objects[4:8]
            SoMi_objects_post = SoMi_objects[8:12]+SoMi_objects[8:12]
            for id in range(8):
                if id < 4:
                    SoMi_objects_pre[id] += 'a'
                    SoMi_objects_treat[id] += 'a'
                    SoMi_objects_post[id] += 'a'
                else:
                    SoMi_objects_pre[id] += 'b'
                    SoMi_objects_treat[id] += 'b'
                    SoMi_objects_post[id] += 'b'
            random.shuffle(SoMi_objects_pre)
            random.shuffle(SoMi_objects_treat)
            random.shuffle(SoMi_objects_post)

            p.participant.objects_pre = SoMi_objects_pre
            p.participant.objects_treat = SoMi_objects_treat
            p.participant.objects_post = SoMi_objects_post

            SoMi_preferences_other = list(map(str, list(range(1, 13))))
            for id in range(12):
                SoMi_preferences_other[id] += random.choice(['a', 'b'])
            print(SoMi_objects_treat)

            p.participant.preferences_other = SoMi_preferences_other

            p.participant.PGG_first = random.choice([True, False])
            p.participant.treatment = random.choice(['SoMi_CG', 'SoMi_EG1', 'SoMi_EG2', 'SoMi_EG3'])


# PAGES
class Introduction1(Page): #Verweis auf html page, die diese Eigenschaften haben soll
    pass

class Introduction2(Page):
    pass

page_sequence = [Introduction1, Introduction2]