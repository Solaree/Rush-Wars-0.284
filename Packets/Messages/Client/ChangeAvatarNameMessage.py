from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommandMessage import *


class ChangeAvatarNameMessage(Reader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.commandID = 3

    def decode(self):
        self.playername = self.readString()

    def process(self, crypter):
        AvailableServerCommandMessage(self.client, self.player, self.commandID).Send(crypter)