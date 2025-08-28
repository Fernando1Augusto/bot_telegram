from telethon import TelegramClient

api_id = 24551106
api_hash = '838d425f82e1912c924a0c0c657cf4f3'
phone = '+5562985161187'
senha_2fa = 'batista16'

client = TelegramClient('minha_sessao', api_id, api_hash)

async def main():
    print("Listando grupos e chats que você participa:\n")
    async for dialog in client.iter_dialogs():
        print(f"{dialog.name} -> {dialog.id}")

# aqui passamos a senha diretamente
client.start(phone=phone, password=senha_2fa)
client.loop.run_until_complete(main())