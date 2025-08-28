from telethon import TelegramClient

api_id = 24551106
api_hash = '838d425f82e1912c924a0c0c657cf4f3'
phone = '+5562985161187'
senha_2fa = 'batista16'

# IDs dos grupos
source_group = -1001712910340  # grupo de origem
target_group = -4697344911     # grupo de destino

client = TelegramClient('minha_sessao', api_id, api_hash)

async def main():
    # Conecta e autentica
    await client.start(phone=phone, password=senha_2fa)
    
    print("Listando grupos e chats que você participa:\n")
    async for dialog in client.iter_dialogs():
        print(f"{dialog.name} -> {dialog.id}")

    print("Iniciando cópia de mídias...")
    async for message in client.iter_messages(source_group):
        if message.media:  # só mídias
            try:
                await client.send_file(target_group, message.media)
                print("Mídia enviada com sucesso")
            except Exception as e:
                print(f"Erro ao enviar: {e}")

with client:
    client.loop.run_until_complete(main())