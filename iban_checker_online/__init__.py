from otree.api import *
import string
import re


def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


_LETTERS = chain(enumerate(string.digits + string.ascii_uppercase),
                 enumerate(string.ascii_lowercase, 10))
LETTERS = {ord(d): str(i) for i, d in _LETTERS}

passphrase = 'ncc1701'

class C(BaseConstants):
    NAME_IN_URL = 'BankDetailsOnline'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name = models.StringField(label='Vorname')
    surname = models.StringField(label='Nachname')
    iban = models.StringField(label='IBAN')


# PAGES
class IBAN(Page):
    form_model = 'player'
    form_fields = ['name', 'surname', 'iban']

    @staticmethod
    def before_next_page(player, timeout_happened):
        import csv, random

        filename = "final_payout_information/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + ".csv"

        header = ['name', 'surname', 'iban', 'payoff']

        with open(filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            payoff = float(player.participant.payoff / 100)
            # write the data
            writer.writerow([player.name, player.surname, player.iban, payoff])

        player.name = '[REDACTED]'
        player.surname = '[REDACTED]'
        player.iban = '[REDACTED]'

class last_page(Page):
    pass

def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)

def generate_iban_check_digits(iban):
    number_iban = _number_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


def iban_error_message(player, my_iban):
    my_iban = my_iban.replace(" ", "")
    pattern = r'[^a-zA-Z0-9]'
    if re.search(pattern, my_iban):
        return 'Please enter a valid IBAN.'
    elif my_iban == passphrase:
        pass
    elif generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban):
        print('IBAN valid \n')
    else:
        return 'Please enter a valid IBAN.'


page_sequence = [
    IBAN,
    last_page
]
