HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["5707627714:AAFHQWTYxUjM8Ee9XvqmOH-uMIgruuzaO84"]
    ARQ_API_KEY = environ["LDWNMP-MJMNBL-BNBCHW-UFPYPA-ARQ"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "5707627714:AAFHQWTYxUjM8Ee9XvqmOH-uMIgruuzaO84"
    ARQ_API_KEY = "LDWNMP-MJMNBL-BNBCHW-UFPYPA-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
