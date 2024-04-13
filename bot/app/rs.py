import sys
import redis
import logging


class Storage:
    def __init__(self, host: str, port: int) -> None:
        self.op = "rs.Storage.init"
        try:
            self.storage = redis.StrictRedis(host=host, port=port)
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            sys.exit(1)

    def checkConnection(self) -> None:
        try:
            logging.info("Redis status: {}".format(self.storage.ping()))
        except Exception as e:
            logging.error("{}: {}".format(self.op, e))
            sys.exit(1)
