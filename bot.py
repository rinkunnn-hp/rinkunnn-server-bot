#references: https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f, https://qiita.com/neight0903/items/b243c730bd09d3562654
# インストールした discord.py を読み込む
import discord
import subprocess
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'THi5IsDuMMyaCCesSTOK3nQ4.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen7kKWs'
# サービスアカウントID
SERVICE_ACCOUNT_ID=hogehoge@hogehoge.iam.gserviceaccount.com
# プロジェクト名
GCP_PROJECT_NAME=hogehoge
# マイクラサーバーインスタンスの名前
MINECRAFT_INSTANCE_NAME=hogehoge
#MINECRAFT_INSTANCE_NAME=minecraft-server
# マイクラサーバーインスタンスのゾーン
MINECRAFT_INSTANCE_ZONE=hogehoge
#MINECRAFT_INSTANCE_ZONE=asia-northeast1-b
# 接続に必要なオブジェクトを生成
client = discord.Client()


#サーバー起動処理
def server_start():
    command = f'screen -S mini java -Xmx1024M -server -jar Geyser.jar nogui'
    subprocess.call(command.split())
    return
#サーバー停止処理
def server_stop():
    command = f'./stop.sh'
    subprocess.call(command.split())
    return
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/server start':
        server_start()
        await message.channel.send('starting server...')
    
    if message.content == '/server stop':
        server_stop()
        await message.channel.send('stopping server...')
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
