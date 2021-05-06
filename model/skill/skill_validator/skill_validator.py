from model.sentence_upload import sentence_converter
from model.skill.skill_validator import validationError


sc = sentence_converter.SentenceConverter()


def check_skill_properties(skill_properties, step):
    if step >= 1:
        try:
            check_general_information(skill_properties)
        except validationError.SkillNameError:
            return validationError.SkillNameError().message
        except validationError.SkillDescriptionError:
            return validationError.SkillDescriptionError().message
    if step >= 2:
        try:
            check_phrases(skill_properties)
        except validationError.SkillEmptyPhrasesError:
            return validationError.SkillEmptyPhrasesError().message

        try:
            check_activators(skill_properties)
        except validationError.SkillEmptyActivatorError:
            return validationError.SkillEmptyActivatorError().message

        try:
            check_phrases_activators(skill_properties)
        except validationError.SkillActionError:
            return validationError.SkillActionError().message
        except validationError.SkillEntityError:
            return validationError.SkillEntityError().message
        except validationError.SkillContextError:
            return validationError.SkillContextError().message

    if step >= 3:
        try:
            check_script(skill_properties)
        except validationError.SkillScriptError:
            return validationError.SkillScriptError().message

    return 'OK'


def check_word_in_sentence(sentence: str, word: str):
    if word == "":
        return True

    words = sc.get_words_from_sentence(sentence)
    word = sc.get_pure_word(word)

    if word in words:
        return True
    else:
        return False


def check_general_information(skill_properties):
    skill_name_validation = check_str_property(skill_properties, 'skillName')
    skill_description_validation = check_str_property(skill_properties, 'skillDescription')

    if (skill_name_validation != -1) and (skill_name_validation != 0):
        raise skill_name_validation from None
    if (skill_description_validation != -1) and (skill_description_validation != 0):
        raise skill_description_validation from None
    return 0


def check_phrases(skill_properties):
    if not('phrases' in skill_properties):
        raise validationError.SkillEmptyPhrasesError() from None
    if type(skill_properties['phrases']) != list:
        raise validationError.SkillEmptyPhrasesError() from None

    phrases = skill_properties['phrases']
    if len(phrases) == 0:
        raise validationError.SkillEmptyPhrasesError() from None
    return 0


def check_activators(skill_properties):
    phrases = skill_properties['phrases']
    for phrase in phrases:
        normalized_action = sc.get_words_from_activators(phrase['action'])
        normalized_entity = sc.get_words_from_activators(phrase['entity'])
        normalized_context = sc.get_words_from_activators(phrase['context'])

        if (len(normalized_action) + len(normalized_entity) + len(normalized_context)) == 0:
            raise validationError.SkillEmptyActivatorError()

    return 0


def check_phrases_activators(skill_properties):
    phrases = skill_properties['phrases']
    for phrase in phrases:
        phrase_text = phrase['phrase']
        normalized_action = sc.get_words_from_activators(phrase['action'])
        normalized_entity = sc.get_words_from_activators(phrase['entity'])
        normalized_context = sc.get_words_from_activators(phrase['context'])

        for action in normalized_action:
            if not(check_word_in_sentence(sentence=phrase_text, word=action)):
                raise validationError.SkillActionError
        for entity in normalized_entity:
            if not(check_word_in_sentence(sentence=phrase_text, word=entity)):
                raise validationError.SkillEntityError
        for context in normalized_context:
            if not(check_word_in_sentence(sentence=phrase_text, word=context)):
                raise validationError.SkillContextError

        return 0


def check_script(skill_properties):
    if 'skillScript' not in skill_properties:
        raise validationError.SkillScriptError from None
    if skill_properties['skillScript'] is None:
        raise validationError.SkillScriptError from None
    return 0


def check_str_property(skill_properties, prop):
    if prop == 'skillName':
        error = validationError.SkillNameError()
    elif prop == 'skillDescription':
        error = validationError.SkillDescriptionError()
    else:
        return -1

    if not(prop in skill_properties):
        return error
    if type(skill_properties[prop]) != str:
        return error
    if len(skill_properties[prop]) == 0:
        return error
    return 0
