#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("12158462")

API_HASH = "0b962717d931f4480c46d56c85d409a5"

BOT_TOKEN = "5989078394:AAFX3-bU_4_8NeM8d2q2TEknJ_SCU45d9GI"

DB_URI = "mongodb+srv://allvipseries:allvipseries@cluster0.k6hza.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQB_aWqYpBzDFc6SfG9Z2QUTc50HlunDgoOTo0X6swjuWwcXEsPE3XsRdot3vZUeE8zHWeYGWGeAKzyon7R8wi80Hi6GtCV_ak_AeC821LLyChIHea3RnijqW_L7fBFZ9yhOVN63iBHgEr6Q_k9_z3uL4lmgUegefcr1hG_Qxk82KAtWz2psYcRcFmIl-CDh2kmW_2qKfvu6XpddejrtKFd0PSOK7-sZrOL8ZBaE85feP2PVWZF3HmTF-Ens9IFdVf44M35OlDIbie7WMZU_QdRijvVtUfTcTtfqhu2-IhVaTsri9vwF8ZnMTWg8U_uLL9OMKoq1HuQ_sYd6Gu5ixrN3UFsxVQA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
