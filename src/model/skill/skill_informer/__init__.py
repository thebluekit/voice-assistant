from model.sentence.converter import SentenceConverter


def get_skill_properties(data):
    skill_properties = {
        "skillName": data["skillName"],
        "skillDescription": data["skillDescription"],
        "skillDate": data["skillDate"],
        "phrases": get_converted_activators(data["phrases"]),
        "skillConstants": data["skillConstants"]
    }
    return skill_properties


def get_converted_activators(phrases):
    sc = SentenceConverter()
    for i in range(len(phrases)):
        normalized_action = sc.get_words_from_activators(phrases[i]['action'])
        normalized_entity = sc.get_words_from_activators(phrases[i]['entity'])
        normalized_context = sc.get_words_from_activators(phrases[i]['context'])

        phrases[i]['normalized_action'] = normalized_action
        phrases[i]['normalized_entity'] = normalized_entity
        phrases[i]['normalized_context'] = normalized_context
    return phrases


def get_skill_script(data):
    skill_file = data["skillScript"]
    return skill_file


def get_skill_step(data):
    skill_step = int(data["skillStep"])
    return skill_step
