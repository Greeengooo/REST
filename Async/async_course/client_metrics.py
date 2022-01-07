import time
import socket
import re
from collections import defaultdict


class Client:
    def __init__(self, host: str, port: int, timeout: int = None):
        self._host = host
        self._port = port
        self._timeout = timeout

    def send_and_fetch(self, message: str) -> str:
        with socket.create_connection((self._host, self._port), self._timeout) as sock:
            sock.sendall(message.encode("utf8"))
            server_response = sock.recv(1024)
            return server_response.decode("utf8")

    def get(self, metric_name: str) -> dict:
        server_response = self.send_and_fetch(f"get {metric_name}\n")
        if server_response == "ok\n\n":
            return {}
        if not self.is_valid_response_data(server_response):
            raise ClientError
        return self.create_dict(server_response)


    def is_valid_response_data(self, response: str) -> bool:
        splitted_response = response.strip().split('\n')
        if splitted_response[0] == "ok":
            return all(
                re.match(r"(.+)\s(\d+\.*\d*)\s(\d+)", i)
                for i in splitted_response[1:]
            )

        return False

    def create_dict(self, response: str) -> dict:
        splitted_response_no_status = response.strip().split('\n')[1:]
        temp = defaultdict(list)
        for elem in splitted_response_no_status:
            metric_name, metric_value, timestamp = elem.split()
            temp[metric_name].append((int(timestamp), float(metric_value)))
        return {key: sorted(val, key=lambda x: x[0]) for key, val in temp.items()}

    def put(self, metric_name: str, metric_value: int, timestamp: int = None) -> None:
        if timestamp is None:
            timestamp = int(time.time())
        server_response = self.send_and_fetch(f"put {metric_name} {metric_value} {timestamp}\n")
        if server_response == 'ok\n\n':
            return
        if not self.is_valid_response_data(server_response):
            raise ClientError
        return


class ClientError(Exception):
    pass


if __name__ == '__main__':
    cl = Client('127.0.0.1', 8888, timeout=15)
    print(cl.get('*'))
