resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def Borrow_Resource():
    input_1 = input("What is your Fellow ID: ")
    input_2 = input("What is your Resource ID: ")
    input_3 = input("What is the Quantity: ")

    if input_1 not in fellows:
        print("Error: Fellow ID does not exit.")
        return
        
    selected_resource = None
    for res in resources:
        if res["id"] == input_2:
            selected_resource = res
            break

    if selected_resource is None:
        print("Error: Resource ID not found.")
        return

    try:
        qyt = int(input_3)
        if qyt <= 0 or qyt > selected_resource["available"]:
            print("Error: Invalid quantity format.")
            return

        selected_resource["available"] -= qyt
        record = {"fellow_id": input_1, "resource_id": input_2, "quantity": qyt}
        borrow_records.append(record)
        print("Success: Resource borrowed successfully!")

    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return

def Return_Resource():
    input_1 = input("What is your Fellow ID: ")
    input_2 = input("What is your Resource ID: ")
    input_3 = input("Enter the Quantity to Return: ")

    if input_1 not in fellows:
        print("Error: Fellow ID does not exit.")
        return

    selected_resource = None
    for source in resources:
        if source["id"] == input_2:
            selected_resource = source
            break

    if selected_resource is None:
        print("Error: Resource ID not found.")
        return

    borrowed_qyt = 0
    for record in borrow_records:
        if record["fellow_id"] == input_1 and record["resource_id"] == input_2:
            borrowed_qyt += record["quantity"] 

    try:
        qyt_to_return = int(input_3)

        if qyt_to_return <= 0:
            print("Error: Return quantity must be a positive integer.")
            return
        if qyt_to_return > borrowed_qyt:
            print(f"Error: You only have {borrowed_qyt} units on loan. Cannot return more than that.")
            return

        selected_resource["available"] += qyt_to_return
        print("Success: Resource returned successfully!")

    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return

def Add_Resource(): pass
def List_Resource(): pass
def Search_Resource(): pass
def Report_Resource(): pass

def main():
    while True:
        print("1. Add Resource")
        print("2. List Resource")
        print("3. Borrow Resource")
        print("4. Return Resource")
        print("5. Search Resource")
        print("6. Report Resource")
        print("7. Exit Resource")

        choice = input("Choose a resource from the listed above: ")

        if choice == "1":
            Add_Resource()
        elif choice == "2":
            List_Resource()
        elif choice == "3":
            Borrow_Resource()
        elif choice == "4":
            Return_Resource()
        elif choice == "5":
            Search_Resource()
        elif choice == "6":
            Report_Resource()
        elif choice == "7":
            print("Exitting...")
            return
        else:
            print("Invalid Resource") 
main()