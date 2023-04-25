import json
from colorama import init, Fore

init(autoreset=True)


class AccessControl:
    def __init__(self):
        self.db = {
            "subjects": {},
            "objects": {},
            "access_matrix": {}
        }
        try:
            with open("database.json", "r") as f:
                self.db = json.load(f)
        except FileNotFoundError:
            pass

    def add_right(self, subj, obj, right):
        if subj not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        if obj not in self.db["objects"]:
            print(Fore.MAGENTA + "Object does not exist.")
            return
        if right not in ["r", "w", "x", "o"]:
            print(Fore.MAGENTA + "Invalid right.")
            return
        if subj not in self.db["access_matrix"]:
            self.db["access_matrix"][subj] = {}
        if obj not in self.db["access_matrix"][subj]:
            self.db["access_matrix"][subj][obj] = []
        if right not in self.db["access_matrix"][subj][obj]:
            self.db["access_matrix"][subj][obj].append(right)
        print(Fore.BLUE + "Right added.")

    def delete_right(self, subj, obj, right):
        if subj not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        if obj not in self.db["objects"]:
            print(Fore.MAGENTA + "Object does not exist.")
            return
        if right not in ["r", "w", "x"]:
            print(Fore.MAGENTA + "Invalid right.")
            return
        if subj in self.db["access_matrix"] and obj in self.db["access_matrix"][subj] and right in \
                self.db["access_matrix"][subj][obj]:
            self.db["access_matrix"][subj][obj].remove(right)
            print(Fore.BLUE + "Right deleted.")
        else:
            print(Fore.MAGENTA + "Subject does not have the specified right on the object.")

    def create_subject(self, subj):
        if subj in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject already exists.")
            return
        self.db["subjects"][subj] = {}
        self.db["access_matrix"][subj] = {}
        print(Fore.BLUE + "Subject created.")

    def create_object(self, obj):
        if obj in self.db["objects"]:
            print(Fore.MAGENTA + "Object already exists.")
            return
        self.db["objects"][obj] = {}
        for subj in self.db["access_matrix"]:
            self.db["access_matrix"][subj][obj] = []
        print(Fore.BLUE + "Object created.")

    def delete_object(self, obj):
        if obj not in self.db["objects"]:
            print(Fore.MAGENTA + "Object does not exist.")
            return
        for subj in self.db["access_matrix"]:
            if obj in self.db["access_matrix"][subj]:
                del self.db["access_matrix"][subj][obj]
        del self.db["objects"][obj]
        print(Fore.BLUE + "Object deleted.")

    def delete_subject(self, subj):
        if subj not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        for obj in self.db["objects"]:
            if subj in self.db["access_matrix"] and obj in self.db["access_matrix"][subj]:
                del self.db["access_matrix"][subj][obj]
                del self.db["subjects"][subj]
                print(Fore.BLUE + "Subject deleted.")

    def cmd_create_file(self, subj, obj):
        if obj in self.db["objects"]:
            print(Fore.MAGENTA + "Object already exists.")
            return
        if subj not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        for subject in self.db["subjects"]:
            if subject == subj:
                self.db["subjects"][subj][obj] = {}
                self.db["objects"][obj] = subj
                self.db["access_matrix"][subj][obj] = ["r", "w", "x", "o"]
            else:
                self.db["subjects"][subject][obj] = {}
                self.db["access_matrix"][subject][obj] = []
        print(Fore.BLUE + "File created.")

    def cmd_delete_file(self, subj, obj):
        if obj not in self.db["objects"]:
            print(Fore.MAGENTA + "Object does not exist.")
            return
        if subj not in self.db["access_matrix"] or obj not in self.db["access_matrix"][subj] or "o" not in \
                self.db["access_matrix"][subj][obj]:
            print(Fore.MAGENTA + "Subject does not have the specified right on the object.")
            return
        for subject in list(self.db["subjects"]):
            if obj in self.db["subjects"][subject]:
                try:
                    del self.db["subjects"][subject][obj]
                except:
                    None
        for subject in list(self.db["access_matrix"]):
            if obj in self.db["access_matrix"][subject]:
                try:
                    del self.db["access_matrix"][subject][obj]
                except:
                    None
        if obj in self.db["objects"]:
            del self.db["objects"][obj]
        AccessControl().delete_object(obj)
        print(Fore.BLUE + "File deleted.")


    def cmd_grant_right(self, s1, s2, o, right):
        if s1 not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        if s2 not in self.db["subjects"]:
            print(Fore.MAGENTA + "Subject does not exist.")
            return
        if o not in self.db["objects"]:
            print(Fore.MAGENTA + "Object does not exist.")
            return
        if right not in ["r", "w", "x", "o"]:
            print(Fore.MAGENTA + "Invalid right.")
            return
        if right not in self.db["access_matrix"][s1][o]:
            print(Fore.MAGENTA + "Subject does not have the specified right on the object.")
            return
        self.db["access_matrix"][s2][o].append(right)
        self.db["access_matrix"][s1][o].remove(right)
        print(Fore.BLUE + "Right granted from {} to {} on {} with {}".format(s1, s2, o, right))

    def save_db(self):
        with open("database.json", "w") as f:
            json.dump(self.db, f)

    def display_db(self):
        with open('database.json', 'r') as f:
            data = json.load(f)
        users = list(data['subjects'].keys())
        objects = list(data['objects'].keys())
        print('Access Matrix:\n')
        print('\t', end='')
        for obj in objects:
            print(obj, '\t', end='')
        print()
        for user in users:
            print(user, '\t', end='')
            for obj in objects:
                if obj in data['access_matrix'][user]:
                    print(data['access_matrix'][user][obj], '\t', end='')
                else:
                    print('-', '\t', end='')
            print()

    def parse_command(self, command_str):
        cmd_parts = command_str.split()
        if len(cmd_parts) < 2:
            print("Invalid command")
            return
        cmd = cmd_parts[0]
        if cmd == "cmd_create_file":
            if len(cmd_parts) < 3:
                print("Invalid command")
                return
            subj = cmd_parts[1]
            obj = cmd_parts[2]
            self.cmd_create_file(subj, obj)
        elif cmd == "cmd_delete_file":
            if len(cmd_parts) < 3:
                print("Invalid command")
                return
            subj = cmd_parts[1]
            obj = cmd_parts[2]
            self.cmd_delete_file(subj, obj)
        elif cmd == "cmd_grant_right":
            if len(cmd_parts) < 4:
                print("Invalid command")
                return
            subj1 = cmd_parts[1]
            subj2 = cmd_parts[2]
            obj = cmd_parts[3]
            right = cmd_parts[4]
            self.cmd_grant_right(subj1, subj2, obj, right)
        else:
            print("Invalid command")

ac = AccessControl()

while True:
    command = input('Input command >>> ')
    if command == "print":
        ac.display_db()
    else:
        ac.parse_command(command)
    ac.save_db()


