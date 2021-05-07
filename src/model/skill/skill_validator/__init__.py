from model.skill.skill_validator import skill_validator


class SkillValidator:
    @staticmethod
    def check_skill(skill_data, skill_step):
        check_data = skill_validator.check_skill_properties(skill_data, skill_step)
        return check_data
