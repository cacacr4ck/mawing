# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from distutils.util import strtobool
from os import getenv
from Uputt.helpers.cmd import cmd

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://raw.githubusercontent.com/cacacr4ck/mawing/main/Uputt/resources/aw.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "9d6c0d3bbf0d37af171330e5b011e2a5")
API_ID = getenv("API_ID", "10345720")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "1665024840")
BOT_TOKEN = getenv("BOT_TOKEN", "6666576153:AAEJVzUuPeEwazyBcr1DWhfjrRNgJvzVByY")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "storybangzul")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "kawasanvillain")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
REPO_URL = getenv("REPO_URL", "https://github.com/cacacr4ck/mawing")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAACcAAMMBL-I_z7I19xCI-AbOA3zcbsMbWzgv69cMCi4ZsMRLf75qzqXm66oObCEx4lrJcVZPY0yJXyvyJW7hNXOaDkVknHcuuR7NMDzSMnBV01xSBUOO95f3cg9bqvzafZtugG6heymJaADhOGNpOCoJnScxpfp6utxpntwi3fSV8KKVw3FWXQpm2Hk-E9PjkKEh_NdjtQJ-8lae3d4Raiy0IMdfaOR7GTrh9jVmZNd4zM_tl0b1ZUx388bO9DaB7xI2OqhKqHg_6D3MNxLKPz_tjD0aVaZypuyzJFE_nOlqT9L_s0CyFE0tSKDaK1y-kJWzTtcDkSJJHuliLRtMvyti_TwAAAABjPkNIAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
