import socketserver

class HTTPRequestHandler(socketserver.StreamRequestHandler):
  def handle(self):
    data = self.rfile.readline().strip()
    print(data)

    f = open('index.html', 'r')

    self.wfile.write(bytes("HTTP/1.1 200 OK\r\n", "utf8"))
    self.wfile.write(bytes("Content-Type: text/html; charset=utf-8\r\n", "utf8"))
    self.wfile.write(bytes("\r\n", "utf8"))
    self.wfile.write(bytes(f.read(), "utf8"))
    
    f.close()

if __name__ == "__main__":
  host, port = "localhost", 0
  server = socketserver.TCPServer((host, port), HTTPRequestHandler)
  ip, port = server.server_address
  print("IP: %s" % ip)
  print("Port: %s" % port)
  server.serve_forever()
