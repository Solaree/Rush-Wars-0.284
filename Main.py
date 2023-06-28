import socket, time; from threading import *

from Logic.Device import Device; from Logic.Player import Players
from Packets.MessageFactory import *; from Core.Crypto import Crypto


class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		self.server.bind((self.ip, self.port))
		print(f"[*] Server started! IP: {self.ip}, Port: {self.port}")
		while True:
			self.server.listen()
			client, address = self.server.accept()
			print(f"[*] New connection! IP: {address[0]}")
			ClientThread(client, address).start()


class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("[*] Received Error!")
				break
			data += s
		return data

	def run(self):
		crypter = Crypto()
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], "big")
					length = int.from_bytes(header[2:5], "big")
					data = self.recvall(length)
					pdata = crypter.decryptClient(packet_id ,data)
					if packet_id in availablePackets:
						print(f"[*] Received packet! ID: {packet_id}")
						message = availablePackets[packet_id](self.client, self.player, pdata)
						message.decode()
						message.process(crypter)
					else:
						print(f"[*] Packet don\'t handled! ID: {packet_id}")
				if time.time() - last_packet > 10:
					print(f"[*] IP: {self.address[0]} disconnected!")
					self.client.close()
					break
		except ConnectionAbortedError:
			print(f"[*] IP: {self.address[0]} disconnected!")
			self.client.close()
		except ConnectionResetError:
			print(f"[*] IP: {self.address[0]} disconnected!")
			self.client.close()
		except TimeoutError:
			print(f"[*] IP: {self.address[0]} disconnected!")
			self.client.close()

if __name__ == "__main__":
	server = Server("0.0.0.0", 9339)
	server.start()