class student:
    def __init__(self,name,address,reg_no,phone_no,branch):
        self.name=name
        self.address=address
        self.reg_no=reg_no
        self.phone_no=phone_no
        self.branch=branch
    def display(self):
        print("----------student details-----------")
        print("name",self.name)
        print("address",self.address)
        print("reg_no",self.reg_no)
        print("phone_no",self.phone_no)
        print("branch",self.branch)
a=student("rahul","thiruvallur",192319010,8825909204,"bme")
s=student("kumaravel","ambur",192319019,6382651627,"bme")
d=student("prabhu","chennai",192319011,9710462461,"bme")
a.display()
s.display()
d.display()