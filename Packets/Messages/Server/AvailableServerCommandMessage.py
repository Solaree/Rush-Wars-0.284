from Utils.Writer import Writer
from Packets.Commands.Server.LogicChangeAvatarNameCommand import LogicChanageAvatarNameCommand


class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.player = player
        self.commandID = commandID
        self.id = 24111

    def encode(self):

        commands = {
            3: LogicChanageAvatarNameCommand
        }

        if self.commandID in commands:
            self.writeInt(self.commandID)
            commands[self.commandID].encode(self)

        else:
            print(f"[*] Cannot create command! ID: {self.commandID}")
        
        print("[*] AvailableServerCommandMessage sent")