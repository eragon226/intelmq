import sys
from intelmq.lib.bot import *
from intelmq.lib.utils import *
from intelmq.lib.event import *
from intelmq.lib.cache import *
import traceback

class DeduplicatorBot(Bot):
    
    def init(self):
        self.cache = Cache(
                            self.parameters.cache_host,
                            self.parameters.cache_port,
                            self.parameters.cache_id,
                            self.parameters.cache_ttl
                          )


    def process(self):
        message = self.receive_message()

        if message:
            try:
                event = Event.from_unicode(message)
                event.clear("observation_time")
                message_hash = hash(event)                            
            except:
                message_hash = hash(message)

            if not self.cache.exists(message_hash):
                self.send_message(message)
                self.cache.set(message_hash, 'hash')
        self.acknowledge_message()


if __name__ == "__main__":
    bot = DeduplicatorBot(sys.argv[1])
    bot.start()
