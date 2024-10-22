from helping.gmail_process import GmailProcessing

if __name__ == '__main__':
    text_from = '<noreply@eu.iit.csu.ru>'
    proces = GmailProcessing()
    proces.filtering_no_reply(text_from)
    proces.hanging_message_labels("TRASH")
