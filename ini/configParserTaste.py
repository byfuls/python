import configparser

config = configparser.ConfigParser()
ret = config.sections()
print(ret)
ret = config.read('system.ini')
print(ret)
ret = config.sections()
print(ret)

ret = config['GATEWAY']
print(ret)
print(f"[GATEWAY] HOST:{ret['HOST']}")
print(f"[GATEWAY] PORT:{ret['PORT']}")
print(f"[GATEWAY] START-ID:{ret['START-ID']}")
print(f"[GATEWAY] COUNT:{ret['COUNT']}")

ret = config['GATEWAY-ROLE']
print(ret)
print(f"[GATEWAY-ROLE] A Group:{ret['AGroup']}")
print(f"[GATEWAY-ROLE] A Group:{ret.get('AGroup')}")
print(f"[GATEWAY-ROLE] B Group:{ret['BGroup']}")
print(f"[GATEWAY-ROLE] C Group:{ret['CGroup']}")

ret = config['VIRTUAL-SIM']
print(ret)
print(f"[VIRTUAL-SIM] START BIND PORT:{ret['START-BIND-PORT']}")

