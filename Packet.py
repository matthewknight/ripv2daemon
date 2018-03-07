
"""
        0              1               2              3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| command (1)   | version (1)   |        must be zero (2)       |
+---------------+---------------+-------------------------------+
|                                                               |
~                        RIP Entry (20)                         ~
|                                                               |
+---------------+---------------+---------------+---------------+


"""
class Packet(object):
    def __init__(self):
        self.command = None
        self.version = 2
        self.router_id = None

