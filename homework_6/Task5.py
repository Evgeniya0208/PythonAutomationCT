class Email:

    def __init__(self, sender, recipient, subject, body):
        self._sender = sender
        self._recipient = recipient
        self._subject = subject
        self._body = body

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    def send(self):
        print(f"From: {self._sender}\nTo: {self._recipient}\nSubject: {self._subject}\nBody: {self._body}")



my_email = Email("jane@ukr.net", "dima@kr.net", "Homework", "My homeworks are in progress")
my_email.send()
