from datetime import datetime
with open('bye.txt','a') as abc:
    while True:
        login=input('login kiriting ')
        parol=input('parol kiriting ')
        time=datetime.now()
        print(time)
        abc.write(f'Login: {login}\n')
        abc.write(f'Parol: {parol}\n')
        q=input('Davom etasizmi Xa   /  Yoq\n')
        abc.write(f'Salom {login} siz {datetime.now()} da tshrif buyurdingiz')
        if q=='Yoq':
            break
