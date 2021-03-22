#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'魔包唤醒'

__author__ = 'WH-2099'

import socket
import re


BROADCAST_IP = '255.255.255.255'
DEFAULT_PORT = 9
MAC_ADDRESS_PATTERN = r'([0-9a-fA-f]{2}[-\s]?){6}'


def magicWakeUp(*macAddressStrs:tuple, ip:str=BROADCAST_IP, port:int=DEFAULT_PORT) -> None:
    pattern = re.compile(MAC_ADDRESS_PATTERN)
    for macAddressStr in macAddressStrs:
        if pattern.fullmatch(macAddressStr):
            macAddressStr = macAddressStr.replace('-', '')
            magicPkgStr = 'FF' * 6 + macAddressStr * 16
            magicPkgBytes = bytes.fromhex(magicPkgStr)
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.sendto(magicPkgBytes, (ip, port))
        

if __name__ == '__main__':
    magicWakeUp('00-D8-61-34-EE-B2')