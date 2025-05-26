TEMPLATE_PATH = "skeaneRW/day24/mail_merge/letters/letter_template"
GUESTS = [
    {"name":"Sarah", "food":"tuna casserole", "additional_note":"don't bring Eliza. She like to gossip."},
    {"name":"Gus", "food":"tofu cake", "additional_note":""},
    {"name":"Fred", "food":"crispy bacon", "additional_note":"bring your chess set in case things quiet down."},
    {"name":"Peter", "food":"ants on a log", "additional_note":"I hope you can come, man. You always bring the party!!!"},
    {"name":"Angie", "food":"lemon fish", "additional_note":"I'm going to wear that hat you got for me when we were in the Mall of America. Good times!"},
]
def get_template():
    with open(TEMPLATE_PATH,mode="r") as file:
        letter_content = file.read()
        lines= letter_content.splitlines('\n')
        parsed_letter = []
        for line in lines:
            parsed_letter.append(line)
        return parsed_letter

def customize_letter(guest):
    template = get_template()
    customized_letter = []
    for line in template:
        for key, _ in guest.items():
            line = line.replace(f"{{{key}}}", guest[key])
        customized_letter.append(line)
    return customized_letter

def write_custom_letter(guest):
    custom_letter = customize_letter(guest)
    with open(f"skeaneRW/day24/mail_merge/letters/party_invite_{guest["name"]}",mode="w") as file:
        file.writelines(custom_letter)

for guest in GUESTS:
    write_custom_letter(guest)








