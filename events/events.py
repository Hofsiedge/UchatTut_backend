import re

class Event:
    def __init__(self):
        self.json_type = '_'.join(
            map(str.lower, re.findall(r'([A-Z][a-z0-9]*)',
                                      self.__class__.__name__)))

    def json_repr(self):
        return ""


class ChatEvent(Event):
    pass


class MessageAction(ChatEvent):
    pass


class ChatAction(ChatEvent):
    pass

