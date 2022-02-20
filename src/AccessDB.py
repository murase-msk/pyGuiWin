import win32com.client


class AccessDB:

    def __init__(self):
        self.__ACCESS_FILE_PATH = 'C:\\Users\\masaki\\Desktop\\test.accdb'
        self.__DSN = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source=' + self.__ACCESS_FILE_PATH + ';'
        # ADODB.Connection
        self.__con = win32com.client.Dispatch('ADODB.Connection')
        self.__con.Open(self.__DSN)
        # ADODB.Recordset
        self.__rs = None

    # DB切断
    def closeDB(self):
        self.__con.Close()

    # データ取得
    def getData(self):
        query = "select * from member"
        self.__rs = self.__con.Execute(query + "' AS Message")[0]

        # レコード数
        # print(rs.RecordCount)

        flds_name = {}
        # flds_value = {}
        fCount = self.__rs.Fields.Count
        for x in range(fCount):
            flds_name[x] = self.__rs.Fields.Item(x).Name

        # フィールド名
        print(flds_name)

        # # 全データをtable_Valueに取得する。
        self.__rs.MoveFirst()
        count = 0
        table_Value = {}
        while True:
            if self.__rs.EOF:
                break
            else:
                flds_Value = {}
                for x in range(fCount):
                    flds_Value[flds_name[x]] = self.__rs.Fields.Item(x).Value
                table_Value[count] = flds_Value
                count = count + 1
                self.__rs.MoveNext()

        print(table_Value)

        # # フィールドの型を表示してみる。
        for x in range(fCount):
            print(type(table_Value[0][flds_name[x]]))

        self.__rs.Close()

    # データ挿入
    def insertData(self):
        query = "insert into member(名前) values('abcd');"
        self.__rs = self.__con.Execute(query)[0]
