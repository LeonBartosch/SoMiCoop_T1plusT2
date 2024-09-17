from os import environ

SESSION_CONFIGS = [
    dict(
        name='Test',
        app_sequence=[
            'introduction',
            'personal_code',
            'SVO_PGG',
            'closing_part',
        ],
        num_demo_participants=8,
        svo_file="SVO_Fullx11.csv",
        use_browser_bots=False
    ),
    dict(
        name='SoMiCoop_T1',
        app_sequence=[
            'T1_introduction',
            'T1_personal_code',
            'T1_hexaco_preferences_svo',
            'T1_attention_check',
            'T1_closing_part'
        ],
        num_demo_participants=1,
        svo_file="SVO_Fullx11.csv"
    ),
    dict(
        name='SoMiCoop_T2',
        app_sequence=[
            'introduction',
            'personal_code',
            'SoMi_Pre',
            'SoMi_CG',
            'SoMi_EG1',
            'SoMi_EG2',
            'SoMi_EG3',
            'SoMi_ManipulationCheck',
            'SoMi_Post',
            'SVO_PGG',
            'demographics_attention',
            'closing_part'
        ],
        num_demo_participants=8,
        svo_file="SVO_Fullx9.csv"
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['personal_code', 'T1_SVO_payoff_self', 'T1_SVO_payoff_other', 'round_numbers', 'objects_pre', 'objects_treat', 'objects_post', 'preferences_other', 'PGG_first', 'treatment', 'PGG_contribution', 'SVO_payoff_self', 'SVO_payoff_other']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'Cents'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1521583681731'
