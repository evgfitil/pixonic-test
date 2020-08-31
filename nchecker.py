import time

import requests


ERROR_STATUSES = [
    400, 403, 404, 405,
    406, 408, 410, 429,
]
WARNING_COUNT = 0


def get_status():
    url = 'http://localhost:80'
    try:
        r = requests.get(url=url)
        status = r.status_code
    except requests.exceptions.RequestException as e:
        return print(e)

    return status


if __name__ == '__main__':

    while True:
        current_status = get_status()
        if current_status == 200:
            print(f'OK: status code {current_status}')
            WARNING_COUNT = 0
        elif current_status in ERROR_STATUSES or WARNING_COUNT > 3:
            print(f'ERROR: status code {current_status}')
        elif current_status in range(500, 505):
            print(f'WARNING: status code {current_status}')
            WARNING_COUNT += 1

        time.sleep(10)
