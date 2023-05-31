# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import Union
import config
from FallenMusic import BOT_USERNAME




def time_to_seconds(time):

    stringt = str(time)

    return sum(

        int(x) * 60**i

        for i, x in enumerate(reversed(stringt.split(":")))

    )

def stream_markup_timer(_, videoid, chat_id, played, dur):

    played_sec = time_to_seconds(played)

    duration_sec = time_to_seconds(dur)

    percentage = (played_sec / duration_sec) * 100

    zenitsu = math.floor(percentage)

    if 0 < zenitsu <= 10:

        bar = "◉—————————"

    elif 10 < zenitsu < 20:

        bar = "—◉————————"

    elif 20 <= zenitsu < 30:

        bar = "——◉———————"

    elif 30 <= zenitsu < 40:

        bar = "———◉——————"

    elif 40 <= zenitsu < 50:

        bar = "————◉—————"

    elif 50 <= zenitsu < 60:

        bar = "—————◉————"

    elif 60 <= zenitsu < 70:

        bar = "——————◉———"

    elif 70 <= zenitsu < 80:

        bar = "———————◉——"

    elif 80 <= zenitsu < 95:

        bar = "————————◉—"

    else:

        bar = "—————————◉"
        
        

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [

            InlineKeyboardButton(

                text=f"{played} {bar} {dur}",

                callback_data="GetTimer",

            )

        ],
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ],
    [

        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=config.SUPPORT_CHAT),

        InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ ↻", callback_data="close"),

    ],
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="✜ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✜",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs •", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="✜ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✜",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="sᴜᴅᴏ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_home"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_help"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]
