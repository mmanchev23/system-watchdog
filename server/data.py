#!/usr/bin/env python3

import time
import requests

if __name__ == "__main__":
    host_id = str(input("Host: "))
    seconds = int(input("Seconds: "))

    for _ in range(seconds):
        response = requests.post("http://localhost:8000/metrics/", json={
            "host_id": host_id,
            "time": seconds
        }).json()

        print(response)
        time.sleep(1)  
