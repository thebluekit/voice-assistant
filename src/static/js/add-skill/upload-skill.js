const addSkillUrl = '/addSkill'

function uploadSkill() {
    // console.log(window.skillObj);
    sendSkill(window.skillObj);
}

function sendSkill(skillProps) {
    var xhr = new XMLHttpRequest();
    var url = addSkillUrl;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Skill status:", xhr.responseText);
            window.skillObj = {
                "skillName": null,
                "skillDescription": null,
                "phrases": [],
                "skillConstants": [],
                "skillScript": null,
                "skillDate": getCurrentDate(),
                "skillStep": 1,
                "skillId": ''
            }
        }
    };
    var data = JSON.stringify(skillProps);
    xhr.send(data);
}