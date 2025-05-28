# EX01 Developing a Simple Webserver
## Date: 14.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```
## OUTPUT:
![alt text](<Screenshot 2025-05-01 205945.png>)

![alt text](<Screenshot 2025-05-01 205851.png>)



## RESULT:
The program for implementing simple webserver is executed successfully.
