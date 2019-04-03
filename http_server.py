#!/usr/bin/env python3
"""
solution for the task04 - code a HTTP server

to exit the running Program just press enter

note for me: curl http://localhost:17300
"""

import http.server
import threading
import random
from multiprocessing import Pool
import urllib.request


PROCESS_AMOUNT = 7


class Handler(http.server.BaseHTTPRequestHandler):
    """
    A customized Handler class to process HTTP requests
    """
    def do_GET(self):  # pylint: disable=snake-case
        """
        custom class to resolve a GET-request
        :return:
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(str(self.server.state).encode("utf-8"))


class Process:  # pylint: disable=too-few-public-methods
    """
    the Process contains and runs the server and also manages it's state
    """
    def __init__(self, process_id, start_port):
        self.process_id = process_id
        self.port = self.process_id + start_port

        self.server = http.server.HTTPServer(('127.0.0.1', self.port), Handler)
        self.server.state = random.randint(0, 9)

        self.server_th = threading.Thread(target=self.server.serve_forever)
        self.server_th.start()

        if self.process_id == 0:
            self.previous_processor = PROCESS_AMOUNT - 1 + start_port
        else:
            self.previous_processor = self.process_id - 1 + start_port

        print('Server is running on Port ', self.port)
        self.compare_state()

    def compare_state(self):
        """
        compares the state of the current to the previous process and takes according actions
        :return:
        """
        # repeat every 0.5 seconds
        threading.Timer(0.5, self.compare_state).start()

        # get state of previous processor
        with urllib.request.urlopen('http://localhost:{0}'
                                    .format(self.previous_processor)) as state:
            previous_state = int(state.read().decode("utf-8"))

        # compare the states
        if self.process_id == 0:
            if self.server.state == previous_state:
                self.server.state = (previous_state + 1) % 10  # set new state
                print("CHANGED state of 127.0.0.1:{0} to {1}".format(self.port, self.server.state))

        elif self.server.state != previous_state:
            self.server.state = previous_state  # set new state
            print("CHANGED state of 127.0.0.1:{0} to {1}"
                  .format(self.port, self.server.state))


def create_processes(process_id):
    """
    creates the processes
    :param process_id:
    :return:
    """
    start_port = 17300
    Process(process_id, start_port)


def main():
    """
    main function
    :return:
    """
    processes = Pool(PROCESS_AMOUNT)
    processes.map(create_processes, range(PROCESS_AMOUNT))

    input("Press <return> to exit")
    processes.close()
    processes.join()


if __name__ == "__main__":
    main()
