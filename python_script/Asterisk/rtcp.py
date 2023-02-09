import asyncio
import time

import panoramisk
from panoramisk import Manager

manager = Manager(loop=asyncio.get_event_loop(),
                  host='192.168.1.3',
                  port=5038,
                  username='admin',
                  secret='1q2w!Q@W',
                  ping_delay=5
                  )


def callback(mngr: panoramisk.Manager, msg: panoramisk.message) -> None:
    """Catch AMI Events/Actions"""

    if msg.event == 'FullyBooted':
        print('Connection OK')

    elif msg.event == "RTCPSent":
        now = time.ctime(float(msg.Timestamp))
        lost = round(int(msg.Report0CumulativeLost) / int(msg.SentPackets) * 100, 2)
        print(f"{now}, Channel: {msg.Channel} SentPackets: {msg.SentPackets}, "
              f"LostPackets: {msg.Report0CumulativeLost}, Lost: {lost}%")


def main(mngr: panoramisk.Manager) -> None:
    mngr.register_event('*', callback=callback)
    mngr.connect()

    try:
        mngr.loop.run_forever()
    except (SystemExit, KeyboardInterrupt):
        mngr.loop.close()
        exit(0)


if __name__ == '__main__':
    main(manager)
