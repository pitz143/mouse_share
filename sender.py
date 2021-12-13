from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('127.0.0.1', 9999)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'stop':
	continue

sender.stop_server()