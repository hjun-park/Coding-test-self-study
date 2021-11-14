# import asyncio
# import platform
# import subprocess
# import time
#
# import aiohttp
# import aioping

#
# async def getPingedHost(host, netTimeout, idx):
#     args = ['ping']
#
#     platformOs = platform.system().lower()
#
#     if platformOs == 'windows':
#         args.extend(['-n', '1'])
#         args.extend(['-w', str(netTimeout * 1000)])
#     elif platformOs in ('linux', 'darwin'):
#         args.extend(['-c', '1'])
#         args.extend(['-W', str(netTimeout)])
#     else:
#         raise NotImplemented('Unsupported OS: {}'.format(platformOs))
#
#     args.append(host)
#     output = ''
#
#     try:
#         outputList = []
#         if platformOs == 'windows':
#             output = subprocess.run(args, check=True, universal_newlines=True,
#                                     stdout=subprocess.PIPE,  # Capture standard out
#                                     stderr=subprocess.STDOUT,  # Capture standard error
#                                     ).stdout
#
#             outputList = str(output).split('\n')
#
#             if output and 'TTL' not in output:
#                 output = False
#         else:
#             subprocess.run(args, check=True)
#
#         output = outputList[2]
#     except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
#     # except
#         output = False
#     # return output
#     with open("ping_result.txt", 'w') as f:
#         f.write(f'{idx}: {output}')
#     print(output)


# async def print_something():
#     print('BBBBBBBBBB')
#
#
# async def main():
#     async with aiohttp.ClientSession() as client:
#         i = 0
#         for _ in range(3):
#             await getPingedHost('8.8.8.1', 3, i)
#             await print_something()
#             i += 1
#
#         print('aaaa')


import asyncio
import aioping
import logging


async def do_ping(host):
    while True:
        try:
            delay = await aioping.ping(host) * 1000
            print("Ping response in %s ms" % delay)

        except TimeoutError:
            print("Timed out")


if __name__ == '__main__':
    # # while True:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    #
    # print('end')
    # # loop.run_in_executor(None, main)


    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(do_ping("8.8.8.1"))

    logging.basicConfig(level=logging.INFO)  # or logging.DEBUG
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioping.verbose_ping("8.8.8.1"))
