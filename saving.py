def writing(username, password):
    print('saving starts')
    f = open('password.txt', "a")
    f.write(username)
    f.write('\n')
    f.write(password)
    f.write('\n')
    print('saving ends')
    f.close
def showing(i):
    print('reading starts')
    f = open('password.txt', "r")
    lines = f.readlines()
    return lines[i]
    print('reading ends')
    f.close






