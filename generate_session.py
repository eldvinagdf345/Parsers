from pyrogram import Client

api_id = int(input("Введите API ID: ").strip())
api_hash = input("Введите API Hash: ").strip()

with Client("my_account", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
    print("\n" + "=" * 60)
    print("Ваш Session String (скопируйте всё, что ниже, целиком):")
    print("=" * 60)
    print(app.export_session_string())
    print("=" * 60)
