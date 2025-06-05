import json
import os.path
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class Server(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    base_dir = os.path.dirname(__file__)

    urls_path = {
        "GET":
            {
                "/catalog": base_dir + "catalog.html",
                "/main": base_dir + "main.html",
                "/category": base_dir + "category.html",
                "/contact": base_dir + "contact.html",
                "default": base_dir + "contact.html",
            },
        "POST": {
            "/add_message": {"message": "success"}
        }
    }

    def do_POST(self):
        """Обрабатываем данные по методу POST"""
        urls_path = self.urls_path["POST"]
        if self.path in urls_path:
            content_length = int(self.headers['Content-Length'])
            user_data = self.rfile.read(content_length).decode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            print(user_data)
            self.wfile.write(json.dumps(urls_path[self.path]).encode("utf-8"))

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        urls_path = self.urls_path["GET"]
        if self.path in urls_path:
            template = urls_path[self.path]
        else:
            template = urls_path["default"]

        with open(template, encoding="utf-8", mode="r") as f:
            self.wfile.write(bytes(f.read(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
