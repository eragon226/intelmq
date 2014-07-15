import sys
import json

from intelmq.lib.bot import *
from intelmq.lib.utils import *
from intelmq.lib.event import *
from intelmq.lib.cache import *


class FileBot(Bot):

    def init(self):
        self.file = open(self.parameters.file, 'a')

    def process(self):
        event = self.receive_message()
        
        if event:
            text = unicode(event).encode('utf-8')
            self.file.write(text)
            self.file.write("\n")
            self.file.flush()
        self.acknowledge_message()


if __name__ == "__main__":
    bot = FileBot(sys.argv[1])
    bot.start()
