class Product:
    def __init__(self, name, price, stock):
        self.name =name
        self.price = price
        self.stock = stock
        self.total = [name, price]
class Cart:
    def __init__(self,userid):
        self.userid = userid
        self.cartitems = {}
        self.prices=[]
    def add(self, item):
        if(item.stock>0):
            try:
                self.cartitems[item.name] += 1
                item.stock-=1
            except KeyError:
                self.cartitems[item.name] = 1
                self.prices.append(item.price)
                item.stock-=1
            print("1 item is added")
        else:
            print("Item is out of stock! Come back later")
    def remove(self,item):
        try:
            if(self.cartitems[item.name] == 1):
                del self.cartitems[item.name]
                self.prices.remove(item.price)
                item.stock+=1
            else:
                self.cartitems[item.name] -= 1
                item.stock+=1
        except KeyError:
            print(f"{item.name} is not present in your cart")

    def showCart(self):
        print(f"--------{self.userid}'s CART--------")
        print("  item  qty price total")
        x =[]
        s = 0
        for i in self.cartitems:
            l = []
            l.append(str(i))
            l.append(self.cartitems[i])
            x.append(l)
        for i in range(len(self.prices)):
            
            x[i].append(self.prices[i])
            x[i].append(self.prices[i]*x[i][1])
        for i in x:
            print(str(i))
            s+=i[3]       
        print("Total payable amount: ",s)
        print("--------------------------")
class Users:
    def __init__(self) -> None:
        self.userslist = {}
        self.logins = 0
    def register(self,name,email, password):
        if email not in self.userslist:
            self.userslist[email] = password
            self.c = Cart(name)
            self.logins = 1
            print("registered successfully. Happy shopping")
        else:
            print("Already registered. Please log in")
    def login(self,email, password):
        if email in self.userslist:
            if(self.userslist[email] == password):
                self.logins = 1
                print("Login successfully. Happy shopping")
            else:
                print("Incorrect password !! Try again")
        else:
            print("Incorrect email Id or not registered yet!!")
    def logout(self, email):
        if(self.logins == 1):
            self.logins = 0
            print(f"{email} Logged out successfully!")

xu = Users()
xu.register("sathvika","girisathvika100@gmail.com","Sath")
xu.login("girsathvika100@gmail.com","Saths")
xu.logout("girsathvika100@gmail.com")
