from simplegmail import Gmail
from simplegmail.label import Label
from simplegmail.message import Message

gmail = Gmail()

class GmailProcessing:
    def __init__(self):
        # непрочитанные сообщения
        self.unread_messages: list[Message] = gmail.get_unread_inbox()
        # все метки
        self.labels: list[Label] = gmail.list_labels()


    def filtering_no_reply(self, sender: str):
        """
        Фильтрация непрочитанных сообщений по заданному отправителю
        :param sender: Строка, которая должна содержаться в поле "Отправитель" в сообщении
        """
        list_of_message_with_noreply = []

        for mail in self.unread_messages:
            if sender in mail.sender:
                list_of_message_with_noreply.append(mail)

        self.unread_messages = list_of_message_with_noreply


    def hanging_message_labels(self, name_of_label: str):
        label = list(filter(lambda x: x.name == name_of_label.upper(), self.labels))

        if label is not []:
            for message in self.unread_messages: message.add_label(label[0])
        else:
            print("Не найдена метка")
