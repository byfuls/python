from smspdu import SMS_SUBMIT
from gsm0338 import Codec


pdu = SMS_SUBMIT.create('sender', 'recipient', 'hello, world')
t = pdu.toPDU()
print(t)

ret = SMS_SUBMIT.fromPDU(1, t, 'sender')
print(ret)
