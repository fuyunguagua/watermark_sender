# -*- coding:utf8 -*-
import requests
import time
from config import host, request_url, payload_original, flag

def watermark_adder(payload, watermark):
    payload_new = payload.copy()
    payload_new[watermark] = flag
    return payload_new

def watermark_maker():
    return 'w'+ str(int(time.time()) / 60 % 100000)

def sender():
    watermark = watermark_maker()
    payload_with_watermark = watermark_adder(payload_original, watermark)
    r = requests.post(host + request_url, data = payload_with_watermark)
    print 'Respose:', r.text
    return watermark

def run(interval, sender):
    index = 1
    while True:
        try:
            watermark = sender()
            print '[watermark] ', watermark, ' posted.'
            index += 1
            time.sleep(interval)
        except Exception as  e:
            print(e)

if __name__ == '__main__':
    run(60, sender)