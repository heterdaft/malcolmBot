from fbchat import Client
from discord import SyncWebhook
import json

# Read Facebook Session Cookies
with open('facebook.cookies', 'r') as f:
    facebook_cookies = json.load(f)

# Read Discord API key from file
with open('discord.control', 'r') as f:
    discord_control = f.read().strip()

with open('discord.proxy', 'r') as f:
    discord_proxy = f.read().strip()

discord_control = SyncWebhook.from_url(discord_control)
discord_proxy = SyncWebhook.from_url(discord_proxy)

# Subclass fbchat.Client and overrides required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # If you're not the author, then handle the message
        if author_id != self.uid:
            # Get known user names
            with open('facebook.users', 'r') as f:
                facebook_users = json.load(f)
            try:
                name = next((n['name'] for n in facebook_users if str(n['id']) == author_id), author_id)
                discord_proxy.send(f"{name}: {message_object.text}")
            except:
                pass

try:
    client = EchoBot("", "", session_cookies=facebook_cookies)
    client.listen()
except KeyboardInterrupt:
    pass
except:
    discord_control.send('Malcolm Proxy had an issue')
