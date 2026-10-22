import pyromod.listen  # noqa: F401

# Import Client directly to avoid a sync-wrapped Client export in some
# Kurigram/Pyrogram development builds.
from pyrogram.client import Client
from pyrogram import filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID

app = Client(
    name="DVIS",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)

filters.sudo = filters.create(
    lambda _, __, m: bool(m.from_user and m.from_user.id in OWNER_ID),
    "SudoFilter",
)
