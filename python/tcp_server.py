import socketserver

class TCPRequestHandler(socketserver.StreamRequestHandler):
  def handle(self):
    self.data = self.rfile.readline().strip()
    print("{} wrote:".format(self.client_address[0]))
    print(self.data)

    self.wfile.write(self.data.upper())

if __name__ == "__main__":
  host, port = "localhost", 0
  server = socketserver.TCPServer((host, port), TCPRequestHandler)
  ip, port = server.server_address
  print("IP: %s" % ip)
  print("Port: %s" % port)

  server.serve_forever()

