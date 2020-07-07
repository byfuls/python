import os

ret1 = os.getenv("GATEWAY_HOME")
print(f'ret: {ret1} type:{type(ret1)}')

print(f'bytes support? {os.supports_bytes_environ}')
ret2 = os.getenvb("GATEWAY_HOME".encode())
print(f'ret: {ret2} type:{type(ret2)}')
