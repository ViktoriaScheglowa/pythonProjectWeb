import os.path
from http.server import BaseHTTPRequestHandler, HTTPServer


# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

#http://localhost:63342/pythonProject/main.html

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    base_dir = os.path.dirname(__file__)
    path_to_file = {
        "GET":
            {
                "/contact": "contact.html",
                "/category": "category.html",
                "/catalog": "catalog.html",
                "/main": "main.html",
                "/default": "contact.html"
            }
    }

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        print(body)
        self.send_response(200)
        self.end_headers()


    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        path_to_file = self.path_to_file["GET"]
        if self.path in path_to_file:
            template = path_to_file[self.path]
        else:
            template = path_to_file["/default"]

        with open(template, encoding="utf-8", mode="r") as f:
            self.wfile.write(bytes(f.read(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
