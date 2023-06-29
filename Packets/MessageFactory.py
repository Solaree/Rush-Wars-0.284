from Packets.Messages.Client.ClientHelloMessage import *
from Packets.Messages.Client.LoginMessage import *
from Packets.Messages.Client.KeepAliveMessage import *
from Packets.Messages.Client.ChangeAvatarNameMessage import *

availablePackets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: ChangeAvatarNameMessage
}