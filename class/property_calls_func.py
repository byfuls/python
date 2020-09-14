
class propertyClass:
	def _sum_def(self, s1, s2):
		return s1+s2

	@property
	def pcs_def(self):
		return self._sum_def(1,2)

cls = propertyClass().pcs_def
print(cls)
