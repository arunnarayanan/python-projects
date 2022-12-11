import datetime

DATE_FIELD = '[DATE]'
PLACE_FIELD = '[PLACE]'
NAME_FIELD = '[NAME]'

with open('./Input/Templates/party_invite_template.txt') as template_file:
    template = template_file.read()

with open('./Input/Names/invitee_names.txt') as invitees_file:
    invitee_list = invitees_file.readlines()
    invitees = []
    ready_2_send_files = []

    for x in invitee_list:
        invitees.append(x.strip('\n'))

    for user in invitees:
        with open(f'./Output/ReadyToSend/{user}.txt', 'w') as f:
            content = template\
                .replace(NAME_FIELD, user.capitalize())\
                .replace(PLACE_FIELD, 'Austin')\
                .replace(DATE_FIELD, datetime.date(2022, 12, 25).strftime('%b %d, %Y'))

            f.write(content)
            print(f'Wrote email to {f.name}')
