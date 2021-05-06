from model.database.cypher import CypherManager
from model.sentence_upload import SentenceManager
from model.skill_installer.skill_installer import install_skill
DB_LINK = "http://localhost:7474/db/data/"
DB_PASSWORD = "12345"


if __name__ == '__main__':
    # install_skill(0)

    cm = CypherManager(DB_LINK, DB_PASSWORD)
    cm.delete_all_nodes()
    db_manager = SentenceManager(cm)

    sen_1 = "Включи, свет в ванной!!!!!"
    action_1 = ['включить']
    entity_1 = ['свет']
    context_1 = ['ванная']

    sen_2 = "Переключи свет в ванной комнате"
    action_2 = ['переключить']
    entity_2 = ['свет']
    context_2 = ['ванная', 'комната']

    cm = CypherManager(DB_LINK, DB_PASSWORD)
    cm.delete_all_nodes()

    db_manager.upload_sentence(sen_1, "test_func", action_1, entity_1, context_1)
    db_manager.upload_sentence(sen_2, "test_func2", action_2, entity_2, context_2)
