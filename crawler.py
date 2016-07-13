
from selectors import DefaultSelector, EVENT_WRITE

class Fetcher:
    def __init__(self, url):
        self.response = b'' # Empty array of bytes.
        self.url = url
        self.sock = None

        def fetch(self):
            self.sock = socket.socket()
            self.sock.setblocking(false)
            try:
                self.sock.connect(('xkcd.com',80))
            except BlockingIOError:
                pass

            selector.register(self.sock.fileno(),
                              EVENT_WRITE,
                              self.connected)

            def connected(self, key, mask):
                print('connected!')
                selector.unregister(key.fd)
                request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
                self.sock.send(request.encode('ascii'))

                selector.register(key.fd, EVENT_READ, self.read_response)

    fetch('www.thinkhowblog.com');
