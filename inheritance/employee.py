class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class sub(employee):
    def __init__(self, name, id,email):
        super().__init__(name, id)
        self.email=email

obj=sub("Nabhya", 100, "nabhya@gmail.com")
print(obj.id, obj.name,obj.email)
