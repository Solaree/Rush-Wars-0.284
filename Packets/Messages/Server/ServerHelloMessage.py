from Utils.Writer import Writer; from os import urandom


class ServerHelloMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20100

    def encode(self):
        self.writeInt(24)
        self.writeBytes(urandom(24))  # SessionKey

        print("[*] ServerHelloMessage sent")