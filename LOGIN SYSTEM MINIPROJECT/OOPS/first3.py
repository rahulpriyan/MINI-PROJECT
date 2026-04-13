class student:
    def __init__(self,mark):
        self.mark=mark
    def update(self,new_mark):
        self.mark=new_mark
    def show(self):
        print("mark:",self.mark)
s1=student(80)
s1.show()
s1.update(95)
s1.show()