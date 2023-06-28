from io import BufferedReader, BytesIO, SEEK_CUR
import zlib


class Reader(BufferedReader):

    def __init__(self, initial_bytes):
        super().__init__(BytesIO(initial_bytes))

    def readByte(self):
        return int.from_bytes(self.read(1), "big")

    def readBool(self):
        if self.readByte:
            return True

        else:
            return False

    def readUInt16(self, length=2):
        return int.from_bytes(self.read(length), "big")

    def readUInt32(self, length=4):
        return int.from_bytes(self.read(length), "big")

    def readInt32(self):
        return self.readVarInt(False)

    def readSInt32(self):
        n = self.readVarInt(False)
        return (((n) >> 1) ^ (-((n) & 1)))

    def readVarInt(self, isRr):
        shift = 0
        result = 0
        while True:
            byte = self.read(1)
            if isRr and shift == 0:
                byte = self.sevenBitRotateLeft(byte)

            i = int.from_bytes(byte, "big")
            result |= (i & 0x7f) << shift
            shift += 7
            if not (i & 0x80):
                break
        return result

    def sevenBitRotateLeft(self, byte):
        n = int.from_bytes(byte, "big")
        seventh = (n & 0x40) >> 6  # Save 7th bit
        msb = (n & 0x80) >> 7  # Save msb
        n = n << 1  # Rotate to the left
        n = n & ~(0x181)  # Clear 8th and 1st bit and 9th if any
        n = n | (msb << 7) | (seventh)  # Insert msb and 6th back in
        return bytes([n])

    def readVInt(self):
        n = self.readVarInt(True)
        return (((n) >> 1) ^ (-((n) & 1)))

    def readLong(self):
        return self.readUInt32(8)

    def readString(self):
        length = self.readUInt32()
        if length == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(length)
            except MemoryError:
                raise IndexError("String out of range")
            else:
                return decoded.decode("utf-8")

    def readCompressedString(self):
        length = int.from_bytes(self.read(4), "big")
        if length == pow(2, 32) - 1:
            return b""
        zlength = int.from_bytes(self.read(4), "little")
        try:
            decoded = zlib.decompress(self.read(length - 4), 15, zlength)
        except MemoryError:
            raise IndexError("String out of range")
        except (ValueError, zlib.error) as e:
            raise IndexError(f"Decompress error: {e}")
        else:
            return decoded

    def readHexa(self, length):
        return self.read(length).hex()

    def peekInt(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")