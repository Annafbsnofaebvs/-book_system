#用户注册

def register():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input('输入确认密码：')

    if password == repassword:
        #保存信息
        with open(r'E:\python project\book\users.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, password))


        print('用户注册成功！')
    else:
        print('密码不一致！')

#用户登录
def login():
    username = input('输入用户名：')
    password = input('输入密码：')

    if username and password:
        with open(r'E:\python project\book\users.txt') as rstream:
            while True:
                user = rstream.readline()
                if not user:
                    print('用户名或者密码输入有误！')
                    break

                input_user = '{} {}\n'.format(username,password)

                if user == input_user:
                    print('用户登录成功！')
                    break

def show_books():
    print('---------------图书馆里面的图书有：----------------')
    with open(r'E:\python project\book\books.txt', 'r', encoding='utf-8') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')
#register()
#login()
show_books()