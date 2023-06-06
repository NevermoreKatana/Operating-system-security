import csv


class Entity:
    def __init__(self, id):
        self.id = id
        self.links = {}

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_links(self):
        return self.links

    def set_links(self, links):
        self.links = links

    def add_to_links(self, entity, value):
        self.links[entity] = value

    def get_link(self, entity):
        return self.links.get(entity)


class Subject(Entity):
    def __init__(self, id):
        super().__init__(id)


class Document(Entity):
    def __init__(self, id):
        super().__init__(id)


rules = ["t", "g", "a"]
documents = {}
subjects = {}
access_graph = []
run_usl = True


def graph_backup():
    with open("Graph1.csv", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(list(documents.keys()))
        writer.writerow(list(subjects.keys()))
        for entity in access_graph:
            if entity:
                line = [entity.get_id()]
                for link, value in entity.get_links().items():
                    line.append(f"{link.get_id()}:{value}")
                writer.writerow(line)


def command_create(mess):
    mess = mess[:-1]
    arguments = mess.split(",")
    if len(arguments) == 4:
        if arguments[0] in rules:
            if arguments[2] not in documents and arguments[2] not in subjects:
                if arguments[1] in documents:
                    if arguments[3] == "s":
                        subject = Subject(arguments[2])
                        subjects[arguments[2]] = subject
                        documents[arguments[1]].add_to_links(subject, arguments[0])
                        print("creating such subject complete\n")
                    elif arguments[3] == "d":
                        document = Document(arguments[2])
                        documents[arguments[2]] = document
                        documents[arguments[1]].add_to_links(Document(arguments[2]), arguments[0])
                        print("creating such document complete\n")
                    else:
                        print("wrong type of entity\n")
                elif arguments[1] in subjects:
                    if arguments[3] == "s":
                        subject = Subject(arguments[2])
                        subjects[arguments[2]] = subject
                        subjects[arguments[1]].add_to_links(subject, arguments[0])
                        print("creating such subject complete\n")
                    elif arguments[3] == "d":
                        document = Document(arguments[2])
                        documents[arguments[2]] = document
                        subjects[arguments[1]].add_to_links(Document(arguments[2]), arguments[0])
                        print("creating such document complete\n")
                    else:
                        print("wrong type of entity\n")
                else:
                    print("such entity does not exist\n")
            else:
                print("such entity exists\n")
        else:
            print("such rule does not exist\n")
    else:
        print("wrong syntax of command\n")
    graph_backup()


def command_delete(mess):
    mess = mess[:-1]
    arguments = mess.split(",")
    if len(arguments) == 2:
        if arguments[0] in documents:
            if arguments[1] in documents:
                d = documents[arguments[1]]
                if documents[arguments[0]].get_link(d) == "a":
                    remove_entity(arguments[1], d)
                    print("remove such document complete\n")
                else:
                    print("have no privileges on this move\n")
            elif arguments[1] in subjects:
                s = subjects[arguments[1]]
                if documents[arguments[0]].get_link(s) == "a":
                    remove_entity(arguments[1], s)
                    print("remove such subject complete\n")
                else:
                    print("have no privileges on this move\n")
            else:
                print("no such entity for remove\n")
        elif arguments[0] in subjects:
            if arguments[1] in documents:
                d = documents[arguments[1]]
                if subjects[arguments[0]].get_link(d) == "a":
                    remove_entity(arguments[1], d)
                    print("remove such document complete\n")
                else:
                    print("have no privileges on this move\n")
            elif arguments[1] in subjects:
                s = subjects[arguments[1]]
                if subjects[arguments[0]].get_link(s) == "a":
                    remove_entity(arguments[1], s)
                    print("remove such subject complete\n")
                else:
                    print("have no privileges on this move\n")
            else:
                print("have no such entity for remove\n")
        else:
            print("have no such entity\n")
    else:
        print("wrong syntax of command\n")
    graph_backup()


def command_take(mess):
    mess = mess[:-1]
    arguments = mess.split(",")
    if arguments[0] in rules:
        if arguments[1] in documents or arguments[1] in subjects:
            if arguments[2] in documents or arguments[2] in subjects:
                if arguments[3] in documents or arguments[3] in subjects:
                    if find_path(arguments[1], arguments[3], arguments[2], "t", arguments[0]):
                        print("yes, this entity can do it\n")
                    else:
                        print("no, this entity can't do it\n")
                else:
                    print("fourth argument is wrong\n")
            else:
                print("third argument is wrong\n")
        else:
            print("second argument is wrong\n")
    else:
        print("first argument is wrong\n")
    graph_backup()


def command_grand(mess):
    mess = mess[:-1]
    arguments = mess.split(",")
    if arguments[0] in rules:
        if arguments[1] in documents or arguments[1] in subjects:
            from_whom = documents.get(arguments[1]) if arguments[1] in documents else subjects.get(arguments[1])
            if arguments[2] in documents or arguments[2] in subjects:
                to_whom = documents.get(arguments[2]) if arguments[2] in documents else subjects.get(arguments[2])
                if arguments[3] in documents or arguments[3] in subjects:
                    on_what = documents.get(arguments[3]) if arguments[3] in documents else subjects.get(arguments[3])
                    if (from_whom.get_link(to_whom) == "g" or from_whom.get_link(to_whom) == "a") and find_ver(from_whom, on_what, arguments[0]):
                        print("yes, this entity can do it\n")
                    else:
                        print("no, this entity can't do it\n")
                else:
                    print("fourth argument is wrong\n")
            else:
                print("third argument is wrong\n")
        else:
            print("second argument is wrong\n")
    else:
        print("first argument is wrong\n")
    graph_backup()


def command_processing(message):
    components = message.split("(")
    if len(components) == 2:
        if components[0] == "/cr":
            command_create(components[1])
        elif components[0] == "/tk":
            command_take(components[1])
        elif components[0] == "/gr":
            command_grand(components[1])
        elif components[0] == "/rm":
            command_delete(components[1])
        else:
            print("no such command1\n")
    else:
        print("no such command\n")


def remove_entity(id, entity):
    if id in documents:
        del documents[id]
    else:
        del subjects[id]

    for e in access_graph:
        if entity in e.links:
            del e.links[entity]

    access_graph.remove(entity)



def unpacking_graph(file):
    global documents, subjects, access_graph
    with open(file, "r") as file_reader:
        line = file_reader.readline().strip().split(";")
        documents = {doc: Document(doc) for doc in line}

        line = file_reader.readline().strip().split(";")
        subjects = {sub: Subject(sub) for sub in line}

        access_graph = []
        entity = None
        ver = None


        for line in file_reader:
            line = line.strip().split(";")
            access_graph.append(documents[line[0]] if line[0] in documents else subjects[line[0]])

            for i in range(1, len(line)):
                ver = line[i].split(":")
                entity = documents[ver[0]] if ver[0] in documents else subjects[ver[0]]
                access_graph[-1].add_to_links(entity, ver[1])


def find_path(first, last, penultimate, f_rule, s_rule):
    run_usl = True
    first_ver = documents[first] if first in documents else subjects[first]
    penultimate_ver = documents[penultimate] if penultimate in documents else subjects[penultimate]
    last_ver = documents[last] if last in documents else subjects[last]

    if penultimate_ver.get_link(last_ver) == s_rule:
        if len(first_ver.links) == 0:
            return False
        else:
            ver = first_ver
            while len(ver.links) == 1:
                if list(ver.links.values())[0] == f_rule:
                    if list(ver.links.keys())[0] == penultimate_ver:
                        return True
                    else:
                        ver = list(ver.links.keys())[0]
                else:
                    return False
            return find_ver(ver, penultimate_ver, f_rule)
    else:
        return False


def find_ver(n_ver, e_ver, rule):
    for ver in n_ver.links.keys():
        if ver.id == e_ver.id:
            if n_ver.get_link(ver) == rule or n_ver.get_link(ver) == "a":
                return True
            else:
                return False
        else:
            if len(ver.links) != 0:
                if find_ver(ver, e_ver, rule):
                    return True
    return False

unpacking_graph("Graph.csv")
message = input()
if message != "/cancel chat":
    login = message

    while message != "/cancel chat":
        print("please write u command:\n")
        message = input()
        # print(message)
        if message != "/cancel chat":
            command_processing(message)
