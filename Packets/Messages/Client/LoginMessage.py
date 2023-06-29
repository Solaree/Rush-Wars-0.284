from Utils.Reader import Reader
from Packets.Messages.Server.LoginOkMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *

class LoginMessage(Reader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.HighID = self.readUInt32()
        self.LowID = self.readUInt32()

        self.Token = self.readString()

        self.MajorVersion = self.readUInt32()
        self.ContentVersion = self.readUInt32()
        self.BuildVersion = self.readUInt32()

        self.ResourceSha = self.readString()
        self.UDID = self.readString()
        self.OpenUDID = self.readString()
        # self.MacAddress = self.ReadString()
        self.DeviceModel = self.readString()

        self.PreferredLanguage = self.readUInt32()

        self.OSLanguage = self.readString()
        self.ADID = self.readString()
        self.OSVersion = self.readString()

        self.UnkBool = self.readBool()  # Unknown
        self.IsAndroid = self.readBool()

        self.IMEI = self.readString()
        self.AndroidID = self.readString()
        self.FacebookAttributionID = self.readString()
        self.IdentifierForVendor = self.readString()

        self.isAdvertiserTrackingEnabled = self.ReadBool()

        self.AppStore = self.ReadUInt32()

        self.KunlunSSO = self.readString()
        self.KunlunUID = self.readString()

        self.UnkInt = self.readUInt32()  # Unknown

    def process(self, crypter):
        print(f"\n------------------------------\n[*] Received Authentication Data:\n------------------------------\nHighID: {self.HighID}\nLowID: {self.LowID}\nPassToken: {self.Token}\nGameVersion: {self.MajorVersion}\nGameBuild: {self.BuildVersion}\nContentVersion: {self.ContentVersion}\nResource SHA: {self.ResourceSha}\nUDID: {self.UDID}\nOpenUDID: {self.OpenUDID}\nDeviceModel: {self.DeviceModel}\nPreferredLanguage: {self.PreferredLanguage}\nOS Language: {self.OSLanguage}\nADID: {self.ADID}\nOSVersion: {self.OSVersion}\nUnknownBool: {self.UnkBool}\nIsAndroid: {self.IsAndroid}\nIMEI: {self.IMEI}\nAndroidID: {self.AndroidID}\nFacebookAttributionID: {self.FacebookAttributionID}\nIdentifierForVendor: {self.IdentifierForVendor}\nisAdvertiserTrackingEnabled: {self.isAdvertiserTrackingEnabled}\nAppStore: {self.AppStore}\nUnknownInt: {self.UnkInt}\n------------------------------\n")

        LoginOkMessage(self.client, self.player).Send(crypter)
        OwnHomeDataMessage(self.client, self.player).Send(crypter)