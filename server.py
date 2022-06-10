import os
import http.server
import socketserver
import json
from web3 import Web3
import boto3
import boto
import boto.s3.connection
from botocore.client import Config
import asyncio
import sched, time
from threading import Thread
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
