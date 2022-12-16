from flask import Flask
import schedule
import time

import notice

# app = Flask(__name__)

# @app.route('/')
# def is_active():
#     schedule.run_pending()
#     return 'line-bot起動中'
    

# schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
# schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
# schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
# schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
# schedule.every().day.at('23:00').do(notice.bed_time_notice)

if __name__ == '__main__':
    schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
    schedule.every().day.at('07:00').do(notice.gomi_check_and_message)
    schedule.every().day.at('08:00').do(notice.gomi_check_and_message)
    schedule.every().day.at('09:00').do(notice.gomi_check_and_message)
    schedule.every().day.at('23:00').do(notice.bed_time_notice)
    schedule.every(2).minutes.do(notice.bed_time_notice)
    # # 60秒おきにジョブの実行条件を満たしているか確認する。
    while True:
        schedule.run_pending()
        # time.sleep(60 * 15)
        time.sleep(60)