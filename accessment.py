resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def add_Resource():
    unique_id = input("What is your unique ID")
    resource_name = input("What is your resource name")
    category = input("What category did you need")
    total_unit = input("What is the total unit")

    for res in resources:
        if unique_id == res["id"]:
            print("Error: Resource ID already exists!")
            return

    try:
        total_unit_int = int(total_unit)
        if total_unit_int <= 0:
            print("Error: Total units must be positive.")
            return

        new_resource = {
            "id": unique_id,
            "name": resource_id,
            "category": category,
            "total": total_unit_int,
            "available": total_unit_int
        }

        resources.append(new_resource)
        print("Success: Resource added successfully!")

    except ValueError:
        print("Error: Total uniits must be a valid integer.")
        return

def list_Resource():
    if resources == "":
        print("No resources is currently regitered.")
        return 

def borrow_Resource():
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

def return_Resource():
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

        for record in borrow_records:
            if record["fellow_id"] == input_1 and record["resource_id"] == input_2:
                record["quantity"] -= qyt_to_return
                if record["quantity"] == 0:
                    borrow_records.remove(record)
                    break

        print("Success: Resource returned successfully!")

    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return

def add_Resource(): pass
def list_Resource(): pass
def search_Resource(): pass
def report_Resource(): pass

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
            add_Resource()
        elif choice == "2":
            list_Resource()
        elif choice == "3":
            borrow_Resource()
        elif choice == "4":
            return_Resource()
        elif choice == "5":
            search_Resource()
        elif choice == "6":
            report_Resource()
        elif choice == "7":
            print("Exitting...")
            return
        else:
            print("Invalid Resource") 
main()