from datetime import date 

products = {}
customers = {}
bills = {}
rewards = {}
pCounter = 0
cCustomer = 0
billCounter = 1

def createProductRepo(pCode, pName, pPrice, pCategory, pCatCode, pDescription, pExpiry):
    global products, pCounter
    temp = {
        "Code" : pCode,
        "Name" : pName,
        "Price" : pPrice,
        "Category" : pCategory,
        "Category Code" : pCatCode,
        "Description" : pDescription,
        "Expiry" : pExpiry
    }
    products[pCounter] = temp
    pCounter = pCounter + 1
    
def createCustomerRepo(cName, cID, cPhone, cAddress, cMail):
    global customers, cCustomer
    temp = {
        "Name" : cName,
        "ID" : cID,
        "Phone" : cPhone,
        "Address" : cAddress,
        "Mail" : cMail
    }
    customers[cCustomer] = temp
    cCustomer = cCustomer + 1

def lookupProductByName(pName):
    global products
    for idx, value in products.items():
        if value["Name"] == pName:
            return value
    return "Product not found"

def lookupCustomerByName(cName):
    global customers
    for idx, value in customers.items():
        if value["Name"] == cName:
            return value
    return "Customer not found"

def lookupCustomerByPhone(cPhone):
    global customers
    for idx, value in customers.items():
        if value["Phone"] == cPhone:
            return value
    return None

def lookupProductByCode(cCode):
    global products
    for idx, value in products.items():
        if value["Code"] == cCode:
            return value
    return None

def lookupBillByBillID(bID):
    global bills
    billDetails = bills.get(bID)
    if billDetails == None:
        print("Bill not found")
        return None
    return billDetails

def lookupBillByCustomerPhone(cPhone):
    global bills
    for idx, value in bills.items():
        if value["Phone"] == cPhone:
            return value
    print("Bill not found")
    return None

def registerProduct():
    print("Enter the product details : ")
    code = int(input("Code: "))
    name = input("Name: ")
    price = float(input("Price: "))
    category = input("Category: ")
    catcode = int(input("Category Code: "))
    desc = input("Description: ")
    expiry = input("Expiry: ")
    createProductRepo(code, name, price, category, catcode, desc, expiry)
    print("Updated Product details!")

def registerCustomer():
    print("Enter customer details: ")
    name = input("Name: ")
    id = int(input("ID: "))
    phone = input("Phone: ")
    address = input("Address: ")
    mail = input("Mail: ")
    createCustomerRepo(name, id, phone, address, mail)
    print("Updated Customer details!")

def productLookUp():
    print("Enter product name to look up: ")
    name = input("Name: ")
    pDetails = lookupProductByName(name)
    print(pDetails)

def customerLookUp():
    print("Enter customer name to look up: ")
    name = input("Name: ")
    cDetails = lookupCustomerByName(name)
    print(cDetails)

def billing():
    global billCounter, bills
    temp = {}
    print("Enter customer phone number to look up: ")
    phone = input("Phone: ")
    customer = lookupCustomerByPhone(phone)
    if customer == None:
        print("Customer not found, registering a new customer")
        registerCustomer()
        print("Enter customer phone number to look up: ")
        phone = input("Phone: ")
        customer = lookupCustomerByPhone(phone)
    temp["Phone"] = phone
    total = 0
    
    customerName = customer["Name"]
    customerCode = customer["ID"]
    currentDate = date.today().strftime("%d/%m/%Y")
    billNumber = billCounter
    billCounter = billCounter + 1
    temp["Name"] = customerName
    temp["Date"] = currentDate


    n = int(input("Enter number of products: "))
    a = []
    for _ in range(n):
        print("Enter product details: ")
        code = int(input("Code: "))
        product = lookupProductByCode(code)
        if product == None:
            print("Product not found")
            return None
        print("Enter product quantity: ")
        qty = int(input("Quantity: "))
        productName = product["Name"]
        productPrice = product["Price"]
        totalCost = productPrice * qty
        total = total + totalCost
        temp[productName] = totalCost
        a.append([productName, "\t", productPrice, "\t", qty, "\t", totalCost])

    print("Bill Number:", billNumber)
    print("Date:", currentDate)
    print("Customer Name:", customerName)
    print("Name", "\t", "Price", "\t", "Quantity", "\t", "Cost")

    for elt in a:
        print(*elt)

    print("Total:", "\t\t", total)
    temp["Total"] = total

    ch = input("Do you want to check for rewards? (Y/N): ")[0].lower()

    if ch == "y":
        rewardAmount = rewards.get(customerCode)
        if rewardAmount == None:
            temp["Rewards"] = rewardAmount
            print("No rewards!")
            print("Reward Amount:", "\t\t", 0)
            print("Grand Total:", "\t\t", total)
        else:
            print("Reward Amount:", "\t\t", rewardAmount)
            temp["Rewards"] = rewardAmount
            total = total - rewardAmount
            rewards[customerCode] = 0
            print("Grand Total:", "\t\t", total)

    temp["Grand Total"] = total
    rewards[customerCode] = total * 0.15 # 15% of totalCost
    bills[billNumber] = temp
    
def searchBills():
    print("Search by")
    print("1. Bill ID")
    print("2. Customer Phone Number")
    
    ch = int(input("Enter choice: "))

    if ch ==  1:
        billId = int(input("Enter bill ID: "))
        billDetails = lookupBillByBillID(billId)
        if billDetails == None:
            return None
        print(billDetails)
    elif ch ==2:
        cPhone = input("Enter customer phone number: ")
        billDetails = lookupBillByCustomerPhone(cPhone)
        if billDetails == None:
            return None
        print(billDetails)
    else:
        print("Try Again!")
        return None

while True:
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Lookup Product")
    print("4. Lookup Customer")
    print("5. Billing")
    print("6. Search Bills")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        registerProduct()

    elif ch == 2:
        registerCustomer()

    elif ch == 3:
        productLookUp()
    
    elif ch == 4:
        customerLookUp()

    elif ch == 5:
        billing()

    elif ch == 6:
        searchBills()
    
    elif ch == 7:
        break
    
    else:
        print("Try Again! ")
        continue



    



