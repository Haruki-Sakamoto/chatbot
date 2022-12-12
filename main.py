import schedule
import time

import notice

if __name__ == '__main__':
    # ジョブを実行する時間を登録する。
    schedule.every(1).minutes.do(notice.bed_time_notice)
    schedule.every().day.at('06:00').do(notice.gomi_check_and_message)
    schedule.every().day.at('23:00').do(notice.bed_time_notice)
    schedule.every().day.at('21:00').do(notice.bed_time_notice)
        
    # 60秒おきにジョブの実行条件を満たしているか確認する。
    while True:
        schedule.run_pending()
        time.sleep(1)