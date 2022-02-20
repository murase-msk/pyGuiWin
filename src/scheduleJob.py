import schedule
import time
import src.Common as Common

# スケジュール実行しているかのフラグ
runningFlg: bool = False


# 定期実行開始関数
def sub():
    # 定期実行関数
    def job():
        Common.win['multiText1'].print('processing job...')

    # 定期実行設定
    schedule.every(5).seconds.do(job)
    # schedule.every(1).minutes.do(job)
    # schedule.every(1).hours.do(job)

    global runningFlg
    runningFlg = True
    while True:
        schedule.run_pending()
        time.sleep(1)
        if not runningFlg:
            break


# ループを終了する
def exitSub():
    global runningFlg
    runningFlg = False
