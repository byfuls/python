from enum import Enum, unique, auto, IntEnum
from datetime import datetime

@unique
#class months(Enum):		Enum 의 열거값과 상수를 비교하면 항상 다르다
class months(IntEnum):		# IntEnum 을 사용하면 열거값과 상수를 비교할 수 있다
	Jan = 1
	Feb = 2
	Mar = 3
	Apr = 4
	May = 5
	Jun = 6
	Jul = 7
	Aug = 8
	Sep = 9
	Oct = 10
	Nov = 11
	Dec = 12

class today:
	def __init__(self):
		self.__now = datetime.now()
		self.__fNow = self.__now.strftime("%Y.%m.%d %H:%M:%s")
		self.__day = self.__now.strftime("%d")
		self.__mon = self.__now.strftime("%m")
		self.__year = self.__now.strftime("%Y")

	@property
	def today(self):
		return self.__fNow
	@property
	def year(self):
		return self.__year
	@property
	def month(self):
		return self.__mon
	@property
	def day(self):
		return self.__day


if __name__ == "__main__":
	t = today()
	print(t.today)
	print(t.month)
	print(t.month)
	print(months.Oct)
	print(type(months.Oct))
	print(repr(months.Oct))

	if int(t.month) == months.Oct:
		print("This month is October")
