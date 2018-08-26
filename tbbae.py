from config import TBBAE_CONFIG
import json, base64
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print('\n###################################################')
print('###### TBBAE  Telegram Bitcoin Bot Auto Earn ######')
print('###### Copyright (C)  2018  Cristian Livella ######')
print('## This program is provided with the MIT License ##')
print('###################################################\n')
print(' ================= Version 1.0.0 ================= \n')

try:
    telegram_session = json.loads(base64.b64decode(TBBAE_CONFIG['telegram_login_key']).decode('utf-8'))
except:
    print('Fatal error 0x02.\nUnable to read telegram_login_key from config.py.\n')
    quit()

string = telegram_session['string_session']
with TelegramClient(StringSession(string), telegram_session['api_id'], telegram_session['api_hash']) as client:
    client.send_message('me', 'Hi')

# TBBAE - Telegram Bitcoin Bot Auto Earn
# Copyright (C) 2018 Cristian Livella

# This program is provided with the MIT License

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://opensource.org/licenses/MIT>.
