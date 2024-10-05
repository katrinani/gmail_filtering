from simplegmail import Gmail
from simplegmail.message import Message

gmail = Gmail()

def filtering_no_reply(sender: str) -> list[Message]:
    """
    Фильтрация непрочитанных сообщений по заданному отправителю
    :param sender: Строка, которая должна содержаться в поле "Отправитель" в сообщении
    :return: Список отфильтрованных сообщений
    """
    list_of_message_with_noreply = []
    mess: list[Message] = gmail.get_unread_inbox()  # непрочитанные сообщения

    for mes in mess:
        if sender in mes.sender:
            list_of_message_with_noreply.append(mes)

    return list_of_message_with_noreply


if __name__ == '__main__':
    text_from = '"Не нужно отвечать на это сообщение (отправлено через eu.iit.csu.ru)" <noreply@eu.iit.csu.ru>'
    filtering_no_reply(text_from)
