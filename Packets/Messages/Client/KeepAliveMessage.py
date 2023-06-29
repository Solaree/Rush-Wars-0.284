from Utils.Reader import Reader
from Packets.Messages.Server.KeepAliveOkMessage import *


class KeepAliveMessage(Reader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        KeepAliveOkMessage(self.client, self.player).Send(crypter)