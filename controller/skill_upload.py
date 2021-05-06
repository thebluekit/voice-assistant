from model.skill.skill_publisher import SkillPublisher
from model.skill.skill_validator import SkillValidator
from model.skill import skill_informer as skill_info


skill_publisher = SkillPublisher()
skill_validator = SkillValidator()


def upload_skill(skill_data):
    publish_status = skill_publisher.upload_skill(skill_data)
    return publish_status


def check_skill(skill_data):
    skill_step = skill_info.get_skill_step(skill_data)
    validation = skill_validator.check_skill(skill_data, skill_step)
    return validation
