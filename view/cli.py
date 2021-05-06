from controller.market import publish_skill
from controller import skill_checker

DELIMITER_LEN = 69


def menu():
    delimiter_start('меню')
    print("1 - Добавить новый навык")
    print("0 - Выход")
    option = input()

    if option == '1':
        add_skill()
    else:
        delimiter_end()
        return 0
    menu()


def add_skill():
    delimiter_start('общие сведения')

    skill_name = input("Введите название навыка: ")
    skill_sentence_flag = True
    skill_sentences = []
    while skill_sentence_flag:

        delimiter_start('добавление предложения')
        skill_sentence = input("Введите предложение, соответствующее этому навыку: ")

        skill_action = add_marking(skill_sentence, 'action')
        skill_entity = add_marking(skill_sentence, 'entity')
        skill_context = add_marking(skill_sentence, 'context')

        add_more = input("Ввести еще предложение? [Y/N]: ")

        skill_sentence_props = {
            "sentence": skill_sentence,
            "skill_action": skill_action,
            "skill_entity": skill_entity,
            "skill_context": skill_context
        }

        skill_sentences.append(skill_sentence_props)

        if not (add_more.lower() == 'y' or add_more.lower() == 'д'):
            skill_sentence_flag = False

    skill_properties = {
        "skill_name": skill_name,
        "skill_sentences": skill_sentences
    }

    publish_skill.skill_upload(skill_properties)


def install_skill():
    pass
    # cm = CypherManager(DB_LINK, DB_PASSWORD)
    # cm.delete_all_nodes()
    # db_manager = SentenceManager(cm)

    # skill_installer = SkillInstaller(db_manager)
    # skill_installer.install('time')


def add_marking(skill_sentence: str, marking_name: str):
    input_text = "Введите " + str(marking_name) + ": "
    ask_input_text = "Ввести еще " + str(marking_name) + "? [Y/N]: "

    marking_flag = True
    markings = []
    while marking_flag:
        check_marking = False
        skill_marking = ""
        while not check_marking:
            skill_marking = input(input_text)
            check_marking = skill_checker.check_word_in_sentence(skill_sentence, skill_marking)
        if skill_marking != "":
            markings.append(skill_marking)

        add_more = input(ask_input_text)
        if not (add_more.lower() == 'y' or add_more.lower() == 'д'):
            marking_flag = False

    return markings


def delimiter_start(title):
    delimiter_symbols = (DELIMITER_LEN - len(title)) // 2
    if (DELIMITER_LEN - len(title)) % 2 == 0:
        print("=" * delimiter_symbols + " " + title.upper() + " " + "=" * delimiter_symbols)
    else:
        print("=" * (delimiter_symbols - 1) + " " + title.upper() + " " + "=" * delimiter_symbols)


def delimiter_end():
    print("=" * (DELIMITER_LEN+1))
