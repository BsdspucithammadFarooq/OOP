class Tenda:
    def __init__(self,x,type):
        self.list=x
        self.type=type
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self,value):
        if value==3 or value==5:
            self._type=value
        else:
            x=int(input("Enter the type again"))
            self.type=x
    def grow(self):
        if len(self.list)==3:
            first_value=self.list[0]+self.list[1]//2
            second_value=self.list[1]+self.list[2]//2
            # for i in range(len(self.list)):
            self.new_tenda=[]
            j=self.list[0]
            self.new_tenda.append(j)
            self.new_tenda.append(first_value)
            j = self.list[1]
            self.new_tenda.append(j)
            self.new_tenda.append(second_value)
            j = self.list[2]
            self.new_tenda.append(j)
    def __str__(self):
        return f"<{self.new_tenda[0]},{self.new_tenda[1]},{self.new_tenda[2]},{self.new_tenda[3]},{self.new_tenda[4]}>"




t=Tenda([1,2,3],4)
t.grow()
print(t)

