import json, base64
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print('\n###################################################')
print('###### TBBAE  Telegram Bitcoin Bot Auto Earn ######')
print('###### Copyright (C)  2018  Cristian Livella ######')
print('## This program is provided with the MIT License ##')
print('###################################################\n')

print('Login at https://my.telegram.org, create an app under')
print('API Development and insert here the required values.\n')

telegram_session = {}
telegram_session['api_id'] = input('App api_id: ')
telegram_session['api_hash'] = input('App api_hash: ')
print()

with TelegramClient(StringSession(), telegram_session['api_id'], telegram_session['api_hash']) as client:
    try:
        telegram_session['strins_session'] = client.session.save()
        print('\nThis is your PERSONAL special login key, you have to put it in config.py.')
        print('Please, DON\'T SHARE this key with anyone!\n')
        print('==> THIS KEY PROVIDES COMPLETE ACCESS TO YOUR TELEGRAM ACCOUNT! <==\n')
        print(base64.b64encode(json.dumps(telegram_session).encode('utf-8').decode('utf-8'))
    except:
        print('Fatal error 0x01.\nUnable to create a Telegram session.\n')

# TBBAE - Telegram Bitcoin Bot Auto Earn
# Copyright (C) 2018 Cristian Livella

# This program is provided with the MIT License

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://opensource.org/licenses/MIT>.
