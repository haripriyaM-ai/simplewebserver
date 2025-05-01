from http.server import HTTPServer, BaseHTTPRequestHandler

html_content = """
<html>
    <head>
        <title>My Book Suggestions</title>
    </head>
    <body bgcolor="#F5F5DC">
        <h1 align="center">My Book Suggestions (Name: Hari Priya Manickam)</h1>
        <hr color="brown">
        <h2>
            <ol>
                <li>To Kill a Mockingbird - Harper Lee</li>
                <li>Ikigai - Francesc Miralles and Hector Garcia</li>
                <li>Harry Potter and the Sorcerer's Stone - J.K. Rowling</li>
                <li>Little Women - Louis May Alcott</li>
                <li>The Alchemist - Paulo Coelho</li>
                <li>1984 - George Orwell</li>
                <li>The Great Gatsby - F.Scott Fitzgerald</li>
                <li>The Psychology of Money - Morgan Housel</li>
                <li>Atomic Habits - James Clear</li>
            </ol>
        </h2>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My Simple book web server is running...")
httpd.serve_forever()


