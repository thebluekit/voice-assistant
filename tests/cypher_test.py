import pytest

from py2neo.database import Graph
from model.database.cypher import CypherManager
from model.database.cypher import cypherError


class TestCypherConnect:
    def test_dotenv_config(self):
        cm = CypherManager()
        assert type(cm.graph) == Graph

    # def test_wrong_password_config(self):
    #     link = "http://localhost:7474/db/data/"
    #     password = "wrong password"
    #
    #     with pytest.raises(cypherError.LoginError):
    #         CypherManager(link, password)

    # def test_wrong_db_link(self):
    #     link = "dblink"
    #     password = "wrong password"
    #
    #     with pytest.raises(cypherError.ConnectionProfileError):
    #         CypherManager(link, password)

    def test_wrong_link_type(self):
        link = 1
        password = "wrong password"

        with pytest.raises(cypherError.ConnectTypeError):
            CypherManager(link, password)

    def test_wrong_password_type(self):
        link = "http://localhost:7474/db/data/"
        password = 1

        with pytest.raises(cypherError.ConnectTypeError):
            CypherManager(link, password)
