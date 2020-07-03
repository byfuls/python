import configparser
from collections import namedtuple

class systemInfo:
	def __init__(self, fileNm):
		config = configparser.ConfigParser()
		config.read('system.ini')
		section = config.sections()

		gw_section = config['GATEWAY']
		gateway = namedtuple('gateway', 'HOST PORT START_ID COUNT')
		self.__gateway = gateway(gw_section.get('HOST'), 
									gw_section.get('PORT'),
									gw_section.get('START-ID'),
									gw_section.get('COUNT'))

		self.__gw_role_section = config['GATEWAY-ROLE']

		virtual_section = config['VIRTUAL-SIM']
		virtual_sim = namedtuple('virtual_sim', 'START_BIND_PORT')
		self.__virtual_sim = virtual_sim(virtual_section.get('START-BIND-PORT'))

	@property
	def gateway(self):
		return self.__gateway
	@property
	def gateway_role(self):
		val = (self.__gw_role_section.get('GROUP')).split(',')
		val[1] = val[1].replace(' ','')

		print(f'val:{val}')
		grouplist = []
		group = namedtuple('group', 'gwcount simxml')
		for i in val:
			sp = i.split(':')
			print(sp)
			groupobj = group(sp[0], sp[1])
			grouplist.append(groupobj)
		print(f'grouplist: {grouplist}')
		return grouplist
	@property
	def virtual_sim(self):
		return self.__virtual_sim

if __name__ == "__main__":
	sys = systemInfo('system.ini')
	#print(sys.gateway)
	#print(sys.gateway.HOST)
	ret = sys.gateway_role[0].gwcount
	print(f'ret:{ret}')
	print(type(ret))
	print(sys.virtual_sim)
	print(sys.virtual_sim.START_BIND_PORT)
