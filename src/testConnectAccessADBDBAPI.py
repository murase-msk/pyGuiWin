from multiprocessing.connection import Connection
from sqlite3 import Cursor
import string
import adodbapi


def main():
    # ACCESS_FILE_PATH = 'test.accdb'
    ACCESS_FILE_PATH: string = 'C:\\Users\\masaki\\Desktop\\test.accdb'
    con_str: string = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source=' + ACCESS_FILE_PATH + ';'
    conn: Connection = adodbapi.connect(con_str)
    cur: Cursor = conn.cursor()

    query: string = "select * from member"
    cur.execute(query)

    for c in cur.fetchall():
        print(c[0])  # => `ringo`, `みかん

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
