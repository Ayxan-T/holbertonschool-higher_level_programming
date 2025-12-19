#!/usr/bin/pyton3
""" Module: task_04_net
    This is a part of the 'Python - Serialization' project.
"""

import socket
import json


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 9999))
        
        s.listen()

        # while True:
        conn, addr = s.accept()

        with conn:
            data = conn.recv(1024)
            json_str = data.decode()
            json_obj = json.loads(json_str)
            print(json_obj)
