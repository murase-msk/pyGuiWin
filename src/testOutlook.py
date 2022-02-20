import win32com.client


# メール関係

# メールフォルダ調べる
def findMailFolder():
    print("ok")
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    # アカウント＋フォルダ＋メール本文
    accounts = outlook.Folders
    print("root (アカウント数=%d)" % accounts.Count)
    for account in accounts:
        print("└ ", account)
        folders = account.Folders
        for folder in folders:
            print("  └ ", folder)
            mails = folder.Items
            for mail in mails:
                print("-----------------")
                print("件名: ", mail.subject)
                print("差出人: %s [%s]" % (mail.sendername, mail.senderEmailAddress))
                print("受信日時: ", mail.receivedtime)
                print("未読: ", mail.Unread)
                print("本文: ", mail.body)


# メール送信
def sendMail():
    # ----------------------------------------
    # Outlookオブジェクトの設定
    # ----------------------------------------
    outlook = win32com.client.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    # ----------------------------------------
    # メール内容の設定
    # ----------------------------------------
    # 署名
    sign = '''
    '''
    mail.bodyformat = 1  # 1:テキスト 2:HTML 3:リッチテキスト
    mail.to = ''
    mail.cc = ''
    mail.bcc = ''
    mail.subject = '件名'
    mail.body = '''
    メール本文
    ''' + '\n' + sign
    # ----------------------------------------
    # 添付ファイルの設定
    # ----------------------------------------
    # 添付ファイルの絶対パス
    add_file1 = 'C:\\...\\...\\file.txt'
    mail.attachments.Add(add_file1)
    # 必要に応じて増やす
    # add_file2 = ''
    # mail.attachments.Add(add_file2)
    # ----------------------------------------
    # メールを送信する
    # ----------------------------------------
    # mail.display(True)
    mail.send()
