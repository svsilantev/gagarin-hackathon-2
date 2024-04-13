import sqlite3
import logging
import sys


class Storage:
    def __init__(self, path: str) -> None:
        self.op = "sqlite.Storage.init"
        try:
            self.conn = sqlite3.connect(path, check_same_thread=False)
            self.cursor = self.conn.cursor()
            logging.info("Storage status: True")
            self.init_tables()
            self.drop_tables()
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            sys.exit(1)

    def drop_tables(self) -> None:
        self.op = "sqlite.Storage.drop_database"
        sqlite_delete_query = """
        DELETE FROM users;
        """
        request = self.cursor.execute(sqlite_delete_query)
        self.conn.commit()

    def init_tables(self) -> None:
        op = "sqlite.Storage.init_tables"

        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          TID INTEGER NOT NULL,
          stage INTEGER NOT NULL);
        """

        try:
            self.cursor.execute(create_users_table)
            logging.info("Tables created")
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            sys.exit(1)

    def is_user_exists(self, user_id: int) -> bool:
        op = "sqlite.Storage.is_user_exists"

        sqlite_select_query = """SELECT * from users WHERE TID = ?"""

        try:
            self.cursor.execute(sqlite_select_query, (user_id,))
            response = self.cursor.fetchall()
            logging.debug("{}: Response: {}".format(op, response))
            if len(response) > 0:
                return True
            else:
                return False
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            return False

    def add_user(self, user_id: int) -> None:
        op = "sqlite.Storage.add_user"

        sqlite_insert_query = """INSERT INTO users (TID, stage) VALUES (?, ?);"""

        try:
            request = self.cursor.execute(sqlite_insert_query, (user_id, 0))
            self.conn.commit()
            logging.debug("Запись {} успешно добавлена в таблицу users".format(user_id))
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))

    def get_user_stage(self, user_id: int) -> int:
        op = "sqlite.Storage.get_user_stage"

        sqlite_select_query = """SELECT stage from users WHERE TID = ?"""

        try:
            self.cursor.execute(sqlite_select_query, (user_id,))
            response = self.cursor.fetchall()
            logging.debug("{}: Response: {}".format(op, response))
            if len(response) > 0:
                return response[0][0]
            else:
                return 0
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            return -1

    def set_user_stage(self, user_id: int, stage: int) -> bool:
        op = "sqlite3.Storage.set_user_stage"

        sqlite_update_query = """Update users set stage = ? where TID = ?"""

        try:
            request = self.cursor.execute(sqlite_update_query, (user_id, stage))
            self.conn.commit()
            logging.debug("Запись {} успешно добавлена в таблицу users".format(user_id))

            return True
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))

            return False
