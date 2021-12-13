from vidstream import StreamingServer
import threading

receiver = StreamingServer('192.168.1.8', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'stop':
	continue

receiver.stop_server()