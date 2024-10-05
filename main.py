from simplegmail import Gmail
from simplegmail.label import Label
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


def hanging_message_labels(list_of_message: list[Message], name_of_label: str) -> None:
    labels = gmail.list_labels()  # все метки

    label: list[Label] = list(filter(lambda x: x.name == name_of_label.upper(), labels))
    if label is not []:
        for message in list_of_message: message.add_label(label[0])
    else:
        print("Не найдена метка")


if __name__ == '__main__':
    text_from = '"Не нужно отвечать на это сообщение (отправлено через eu.iit.csu.ru)" <noreply@eu.iit.csu.ru>'
    mes = filtering_no_reply(text_from)
    hanging_message_labels(mes, "TRASH")
