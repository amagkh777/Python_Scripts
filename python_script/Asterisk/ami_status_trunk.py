import asyncio
import panoramisk
from panoramisk import Manager

manager = Manager(loop=asyncio.get_event_loop(),
                  host='192.168.1.3',
                  port=5038,
                  username='admin',
                  secret='1q2w!Q@W',
                  ping_delay=5
                  )
async def callback(mngr: panoramisk.Manager, msg: panoramisk.message) -> None:
    """Catch AMI Events/Actions"""

    # print(msg)
    if msg.event == 'FullyBooted':
        print('Connection OK')

    elif msg.event == "Registry":
        sample = open('samplefile.txt', 'w')
        print(f"Trunk {msg.Username} status is {msg.Status}",file=sample)
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