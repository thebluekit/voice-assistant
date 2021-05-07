from dotenv import load_dotenv
from string import Template
import postgresError
import psycopg2
import os


class PostgresManager:
    cur = None

    def __init__(self, host: str = None, user: str = None, password: str = None):
        self.cur = self.__connection(host, user, password)

    def __connection(self, host: str = None, user: str = None, password: str = None):
        expected_type = 'str'

        if host is None or user is None or password is None:
            host, user, password = self.__load_from_dotenv()

        if type(host) is not str:
            given_type = str(type(host).__name__)
            raise postgresError.ConnectTypeError("database host type", expected_type, given_type)
        if type(user) is not str:
            given_type = str(type(user).__name__)
            raise postgresError.ConnectTypeError("database user type", expected_type, given_type)
        if type(password) is not str:
            given_type = str(type(password).__name__)
            raise postgresError.ConnectTypeError("database password type", expected_type, given_type)

        try:
            conn = psycopg2.connect(host=host, user=user, password=password)
            cur = conn.cursor()
            return cur
        except Exception as ex:
            raise ex

    @staticmethod
    def __load_from_dotenv():
        load_dotenv()
        host = os.getenv("POSTGRES_HOST")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")

        return host, user, password

    def direct_query(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        print("\nShow me the databases:\n")
        for row in rows:
            print("   ", row[0])