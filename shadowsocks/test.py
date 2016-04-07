import packet

def print_bytes(data):
    print(['{:02x}'.format(ord(d)) for d in data])

a = packet.PacketStream()

data = a.parse(b'\x00\x00\x00\x03\x00\x01\x01\x02\x03\x04\x05')

print_bytes(packet.make(12, b'\x01\x02\x03\x04\x05'))

print(data)
