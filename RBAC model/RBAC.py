import json

def load_data():
    with open("roles.json") as json_file:
        data = json.load(json_file)
        return data

def save_data(data):
    with open("roles_out.json", "w") as json_file:
        json.dump(data, json_file)

def create_role(data):
    role_name = input("Enter role name: ")

    if role_name in data["roles"]:
        print("Error: Role already exists.")
        return

    role = {
        "name": role_name,
        "subjects": [],
        "objects": []
    }

    parent_roles = input("Enter parent roles (comma-separated): ").split(",")
    parent_subjects = set()

    for parent_role in parent_roles:
        if parent_role in data["roles"]:
            parent_subjects.update(data["roles"][parent_role]["subjects"])
        else:
            print(f"Error: Parent role '{parent_role}' does not exist.")
            return

    print("Common subjects from parent roles:", parent_subjects)

    subjects = input("Enter subjects (comma-separated): ").split(",")

    for subject in subjects:
        if subject not in data["subjects"]:
            print(f"Error: Subject '{subject}' does not exist.")
            return
        if subject not in parent_subjects:
            print(f"Error: Subject '{subject}' is not a common subject from parent roles.")
            return

    role["subjects"] = subjects

    objects = []

    while True:
        object_name = input("Enter object name (or 'done' to finish): ")

        if object_name == "done":
            break

        if object_name not in data["objects"]:
            print(f"Error: Object '{object_name}' does not exist.")
            return

        parent_permissions = set()

        for parent_role in parent_roles:
            if parent_role in data["roles"]:
                parent_permissions.update(data["roles"][parent_role]["objects"].get(object_name, []))

        available_permissions = data["objects"][object_name]["permissions"]
        print("Available permissions:", available_permissions)

        permissions = input("Enter permissions (comma-separated): ").split(",")

        for permission in permissions:
            if permission not in available_permissions:
                print(f"Error: Permission '{permission}' is not available for object '{object_name}'.")
                return
            if permission not in parent_permissions:
                print(f"Error: Permission '{permission}' is not inherited from parent roles.")
                return

        additional_permissions = input("Enter additional permissions (comma-separated): ").split(",")
        permissions.extend(additional_permissions)

        objects.append({
            "name": object_name,
            "permissions": permissions
        })

    role["objects"] = objects

    data["roles"][role_name] = role
    save_data(data)
    print("Success")

def main():
    data = load_data()
    create_role(data)
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
