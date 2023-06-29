from Utils.Writer import Writer
from Packets.Messages.Client.ChangeAvatarNameMessage import *

class LogicChanageAvatarNameCommand(Writer):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.playername = playername

    def encode(self):
        self.writeString(self.playername)  # Name