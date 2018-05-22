def check_space(username):
    for x in username:
        if x == ' ':
            return False

    return True


m = check_space('amirmubarak')

if m:
    print('True')
else:
    print('False')
