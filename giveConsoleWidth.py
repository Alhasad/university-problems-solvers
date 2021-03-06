#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
        Returns width of the active console.
'''

def main():
    """ Main method """
    width = 0
    try:
        import struct, fcntl, termios
        s = struct.pack('HHHH', 0, 0, 0, 0)
        x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
        width = struct.unpack('HHHH', x)[1]
    except:
        pass

    if width == 0:
        try:
            width = int(os.environ['COLUMNS'])
        except:
            pass
    if width == 0:
        width = 80

    return width
