import csv


def load_access_matrix(filename):
    access_matrix = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        subjects = next(reader)[1:]
        for row in reader:
            subject = row[0]
            access_matrix[subject] = {}
            for i, value in enumerate(row[1:]):
                object_name = subjects[i]
                access_matrix[subject][object_name] = value
    return access_matrix


def save_access_matrix(filename, access_matrix):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        subjects = [''] + list(access_matrix.keys())
        writer.writerow(subjects)
        for object_name, access in access_matrix.items():
            row = [object_name] + [access[subject] for subject in subjects[1:]]
            writer.writerow(row)


def load_object_secrecy_levels(filename):
    object_secrecy_levels = {}
    with open(filename, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
            else:
                parts = line.split('=')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                key = key.strip()
                value = value.strip()
                if section not in object_secrecy_levels:
                    object_secrecy_levels[section] = {}
                object_secrecy_levels[section][key] = value
    return object_secrecy_levels


def load_subject_secrecy_levels(filename):
    subject_secrecy_levels = {}
    with open(filename, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
            else:
                parts = line.split('=')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if section not in subject_secrecy_levels:
                        subject_secrecy_levels[section] = {}
                    subject_secrecy_levels[section][key] = value
    return subject_secrecy_levels


def update_access_matrix_write(access_matrix, subject, object_name):
    access_matrix[subject][object_name] = {
        'tempSecrecyLevel': subject_secrecy_levels[subject]['tempSecrecyLevel'],
        'permission': 'w'
    }
    return access_matrix


def update_access_matrix_read(access_matrix, subject, object_name):
    if access_matrix[subject][object_name] == 'r':
        access_matrix[subject][object_name] = 'r'
    else:
        access_matrix[subject][object_name] = 'r'
    return access_matrix



access_matrix = load_access_matrix('accessMatrix.csv')

object_secrecy_levels = load_object_secrecy_levels('objects.ini')

subject_secrecy_levels = load_subject_secrecy_levels('subjects.ini')


def process_read_command(command, access_matrix):
    parts = command.split(',')
    if len(parts) == 3:
        subject = parts[0].strip()
        object_name = parts[1].strip()
        permission = parts[2].strip()

        if (
            subject in access_matrix and
            object_name in access_matrix[subject] and
            object_secrecy_levels.get(object_name, {}).get('secrecyLevel') <= subject_secrecy_levels.get(subject, {}).get('secrecyLevel')
        ):
            access_matrix = update_access_matrix_read(access_matrix, subject, object_name)
            print("Разрешено чтение файла.")
        else:
            print("Недостаточно прав для чтения файла.")


def process_write_command(command, access_matrix):
    parts = command.split(',')
    if len(parts) == 3:
        subject = parts[0].strip()
        object_name = parts[1].strip()
        permission = parts[2].strip()

        if (
            subject in access_matrix and
            object_name in access_matrix[subject] and
            subject_secrecy_levels.get(subject, {}).get('secrecyLevel') >= object_secrecy_levels.get(object_name, {}).get('secrecyLevel')
        ):
            access_matrix = update_access_matrix_write(access_matrix, subject, object_name)
            print("Файл успешно записан.")
        else:
            print("Недостаточно прав для записи файла.")


while True:
    command = input("Введите команду (например, read(subject1,file1,r) или write(subject2,object1,w)): ")

    if command.startswith("read"):
        process_read_command(command[5:].strip(), access_matrix)
    elif command.startswith("write"):
        process_write_command(command[6:].strip(), access_matrix)
    elif command == "exit":
        break
    else:
        print("Неверная команда.")


save_access_matrix('acessMatrix.csv', access_matrix)
