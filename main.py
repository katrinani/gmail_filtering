from email.message import Message

from simplegmail import Gmail


def print_hi():
    gmail = Gmail()

    mess = gmail.get_starred_messages()
    for mes in mess:
        print(mes.recipient, mes.sender, mes.subject, mes.date, mes.snippet, mes.plain)


if __name__ == '__main__':
    print_hi()
