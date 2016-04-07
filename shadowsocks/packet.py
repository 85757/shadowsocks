import struct


def make(session, buffer):
	l = len(buffer)
	assert(l <= 0xFFFFFFFF)
	assert(session <= 0xFFFF)
	return struct.pack(">IH", l, session) + buffer;

class PacketStream(object) :
	
	def __init__(self) :
		self._last_buffer = ""

	def parse(self, buffer = None):
		"""
		this function adds buffer to the PacketStream from which we try to parse a packet
		returns session, data and stores remained data
		if Param(buffer) is not long enough to be parsed as a complete packet, None is returned
		"""

		if buffer:
			self._last_buffer = self._last_buffer + buffer;

		l = len(self._last_buffer)

		if l < 6 :
			return None, None
		else:
			datalen, session = struct.unpack(">IH", buffer[:6])
			if datalen <=  l - 6 :
				data = self._last_buffer[6 : 6 + datalen]
				self._last_buffer = self._last_buffer[6 + datalen :]
				return session, data
			else :
				return None, None

