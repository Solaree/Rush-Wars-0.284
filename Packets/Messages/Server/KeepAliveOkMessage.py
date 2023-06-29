from Utils.Writer import Writer


class KeepAliveOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20108

    def encode(self):
        pass

        print("[*] KeepAliveOkMessage sent")