from Utils.Reader import Reader
from Packets.Messages.Server.ServerHelloMessage import *


class ClientHelloMessage(Reader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Protocol = self.readUInt32()
        self.KeyVersion = self.readUInt32()
        self.MajorVersion = self.readUInt32()
        self.BuildVersion = self.readUInt32()
        self.ContentVersion = self.readUInt32()
        self.Hash = self.readString()
        self.Device = self.readUInt32()
        self.Store = self.readUInt32()

    def process(self, crypter):
        print(f"\n------------------------------\n[*] Received Session Data:\n------------------------------\nProtocol: {self.Protocol}\nPepperKeyVersion: {self.KeyVersion}\nGameVersion: {self.MajorVersion}\nGameBuild: {self.BuildVersion}\nContentVersion: {self.ContentVersion}\nHash: {self.Hash}\nDevice: {self.Device}\nStore: {self.Store}\n------------------------------\n")

        ServerHelloMessage(self.client, self.player).Send(crypter)