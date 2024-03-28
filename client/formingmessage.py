

class Message:
    def __init__(self, msg, broker, topic):
        self.message = msg
        self.broker = broker
        self.topic = topic

    def gen_message(self):
        return str(self.topic) + "\\" + str(self.message)
