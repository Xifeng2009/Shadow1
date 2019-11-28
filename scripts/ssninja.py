#! /usr/bin/python3
#! coding:      utf-8
#! Date:        2019-11-28
#! Author:      Rea$on
#! Describe:    Auto Modify Shadowsocks Port and Restart

import os
import json
import random

def main():

    conf = {
            'server': '104.207.133.99',
            'server_port': 1080,
            'local_address': '127.0.0.1',
            'local_port': 1080,
            'password': 'n1nja!!!',
            'timeout': 5,
            'method': 'aes-192-cfb',
            'fast_open': True
        }
    fpath = '/etc/shadowsocks.json'

    conf['server_port'] += random.randint(1,30000)
    print(f"[ServerPort] {conf['server_port']}")

    with open(fpath, 'w') as f:
        json.dump(conf, f, indent=4, ensure_ascii=False) 
    print(f"[SERVER] {conf['server']}")
    print(f"[PORT]   {conf['server_port']}")
    print(f"[METHOD] {conf['method']}")
    print("[WRITTEN] Finished.")
    os.system("ssserver -c /etc/shadowsocks.json -d restart")

if __name__ == '__main__':
    main()
