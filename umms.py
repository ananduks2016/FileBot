"""Emoji

Available Commands:

.umms"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "think":
        await event.edit(input_str)
        animation_chars = [
            "ANANDUS",
            "PINKUS",
            "ANANDUS😍😍😘",
            "KAVYA🧡🧡",
            "LOVE💕💕💕*",
            "ANANDUS💖",
            "LOVE FOR EVER",
            "UMMMMMMMAHH",
            "MICHU👁️👁️",
            "LUB",
            "you",
            "KAVU*",
            "LOVE FOR EVER AND EVER",
            "T+I#K@₹G",
            "SEE YA",
            "ഒരു ഉമ്മ",
            "തരുവോ",
            "¶H×NK&N*",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
