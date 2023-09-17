import json
import random
from art import *

##Auxiliar functions
def generatePrice():
    result = (random.random()*random.randint(20,500))
    while (result < 0.1):
         result == (random.random()*random.randint(20,500))
    
    return result
 
def generateQuantity():
     return random.randint(1,100)

##Classes
class manageProducts:
    def __init__ (self, ProductsLT):
        self.ProductsLT = [()]
        self.ProductsLT = ProductsLT
    
    def __str__(self):
         jsonString = json.dumps(self.__dict__, ensure_ascii=False)
         return (
              f"{jsonString}"
         )
    
    ##CRUD functions
    def listProducts (self):
        print("-"*51)
        print(f"{'ID':<3}{'Product':<30}{'Price $ ':10}{'Quantity':10}")
        print("-"*51)
        for index, product in enumerate(self.ProductsLT):
             print(
                 f"{index:<3}{product[0]:<30}"
                 f"{product[1]:<10}"
                 f"{product[2]:<10}"
                )
        print("-"*51)

             
    def addProduct(self,name,price,quantity):
        self.ProductsLT.append((name, price, quantity))
        self.listProducts()
    
    def updateQuantity(self, id, quantity):
        self.ProductsLT.insert(id, (self.ProductsLT[id][0],self.ProductsLT[id][1], quantity))
        self.ProductsLT.pop(id + 1)
        self.listProducts()
    
    def deleteProduct(self, id):
         self.ProductsLT.pop(id)
         self.listProducts()

##Methods   
def main():
    status = True
    selection = ""
    tprint("             DOOM\nPRODUCTS", font="doom")
    productos = manageProducts([("Fists",round(generatePrice(),2),generateQuantity()),
                                ("Chainsaw",round(generatePrice(),2),generateQuantity()),
                                 ("Shotgun",round(generatePrice(),2),generateQuantity()),
                                 ("Plasma gun",round(generatePrice(),2),generateQuantity()),
                                 ("BFG9000",round(generatePrice(),2),generateQuantity())]
                                 )
    ##Program Loop
    while(status):
        print(
        f"\nSelect an option \n"
        f"1: Get stock \n2: Add a new product \n3: Modify product quantity (ID, Quantity) \n4: Delete an element (Name)\n"
        f"0: Exit"
        )

        selection = input("\nSelect an option: ")
        print()

        ##Switch Case        
        match selection:
            case "1":
                productos.listProducts()
            
            case "2":
                print(f"Insert product: ")
                productos.addProduct(input("Insert name: "), input("Insert price: "), input("Insert quantity: "))

            case "3":
                print(f"Modify product quantity: ")
                productos.updateQuantity(int(input("Insert ID: ")), input("Insert Quantity: "))
            
            case "4":
                  print(f"Delete an element by ID: ")
                  productos.deleteProduct(int(input("Insert ID: ")))

            case "0":
                status = False    

##Call to main method
if __name__ == "__main__":
        main()
