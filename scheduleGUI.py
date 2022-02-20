import PySimpleGUI as sg
import threading
import src.scheduleJob as scheduleJob
import src.Common as Common


def main():
    # 画面レイアウトを指定 ---- (*1)
    layout = [
        [
            sg.Button('開始', size=(30, 3), key='Button1'),
            sg.Button('終了', size=(30, 3), key='Button2')
        ],
        [
            sg.Multiline(default_text="", size=(100, 10), key='multiText1')
        ],
    ]

    startJob()

    # イベントループ --- (*2)
    Common.win = sg.Window('ウィンドウタイトル', layout)
    while True:
        event, values = Common.win.read(timeout=None)
        if event is None:
            break
        if event == 'Button1':
            # Button1処理
            if not scheduleJob.runningFlg:
                Common.win['multiText1'].print('実行中です')
                startJob()
            else:
                Common.win['multiText1'].print('実行中です')
        if event == 'Button2':
            Common.win['multiText1'].print('終了しました')
            scheduleJob.exitSub()


# 初期処理
def startJob():
    threading.Thread(target=scheduleJob.sub, daemon=True).start()


if __name__ == "__main__":
    main()
