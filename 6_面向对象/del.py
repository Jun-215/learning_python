class Car:

    def __init__(self):
        self.name = "小米"
        self.color = "green"

    def __str__(self):
        return (f"name:{self.name},color:{self.color}")
    
    def __del__(self):
        print("清理资源")

mycar = Car()
print(mycar)
