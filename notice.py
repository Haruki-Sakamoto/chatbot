from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
from dotenv import load_dotenv
import datetime as dt
import locale

# line-botのアクセストークンとチャンネルシークレットを.envから受け取る。
load_dotenv()
line_bot_api = LineBotApi(os.getenv('ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

# 曜日を確認して、出すゴミをユーザーに通知する
def gomi_check_and_message():

    # 日本の標準時を取得する。
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    today = dt.datetime.now()
    
    # 今日の曜日を数字で取得する。
    week_num = today.weekday()
    week_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']
    greet = 'おはよ〜'

    if(week_num == 0 or week_num == 3):
        message=f'{greet}\n今日は{week_list[week_num]}だから、\n可燃ごみを出す日だよ！'
    elif(week_num == 1):
        message=f'{greet}\n今日は{week_list[week_num]}だから、\n缶類ごみを出す日だよ！'
    elif(week_num == 2):
        message=f'{greet}\n今日は{week_list[week_num]}だから、\nベットボトル類を出す日だよ！'
    else:
        message=f'{greet}\n今日は{week_list[week_num]}だから、\nゴミを出す日じゃないよー！'
    line_bot_api.broadcast(TextMessage(text=message))
    
    return "通知完了"

# ユーザーに寝る時間の通知をする。
def bed_time_notice():
    message = 'もう寝る時間だ！！！！！\n携帯を閉じろ！！！！！'
    line_bot_api.broadcast(TextMessage(text=message))