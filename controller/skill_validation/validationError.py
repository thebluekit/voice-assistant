from controller.skill_validation import validation_messages


class SkillNameError(Exception):
    def __init__(self, message=validation_messages.SKILL_NAME_ERROR):
        self.message = message
        super().__init__(self.message)


class SkillDescriptionError(Exception):
    def __init__(self, message=validation_messages.SKILL_DESCRIPTION_ERROR):
        self.message = message
        super().__init__(self.message)


class SkillEmptyPhrasesError(Exception):
    def __init__(self, message=validation_messages.SKILL_EMPTY_PHRASES_ERROR):
        self.message = message
        super().__init__(self.message)


class SkillEmptyActivatorError(Exception):
    def __init__(self, message=validation_messages.SKILL_EMPTY_ACTIVATOR_ERROR):
        self.message = message
        super().__init__(self.message)


class SkillActionError(Exception):
    def __init__(self, message=validation_messages.WRONG_ACTION):
        self.message = message
        super().__init__(self.message)


class SkillEntityError(Exception):
    def __init__(self, message=validation_messages.WRONG_ENTITY):
        self.message = message
        super().__init__(self.message)


class SkillContextError(Exception):
    def __init__(self, message=validation_messages.WRONG_CONTEXT):
        self.message = message
        super().__init__(self.message)


class SkillScriptError(Exception):
    def __init__(self, message=validation_messages.SKILL_SCRIPT_EMPTY_ERROR):
        self.message = message
        super().__init__(self.message)
