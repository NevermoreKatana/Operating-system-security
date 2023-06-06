import csv
from configparser import ConfigParser

# Загрузка матрицы доступа из accessMatrix.csv
def load_access_matrix(file_path):
    access_matrix = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        for row in reader:
            subject = row[0]
            access_matrix[subject] = {}
            for i in range(1, len(headers)):
                access_matrix[subject][headers[i]] = row[i]
    return access_matrix

# Загрузка атрибутов объектов из objects.ini
def load_object_attributes(file_path):
    config = ConfigParser()
    config.read(file_path)
    objects = {}
    for section in config.sections():
        objects[section] = dict(config.items(section))
    return objects

# Загрузка атрибутов субъектов из subjects.ini
def load_subject_attributes(file_path):
    config = ConfigParser()
    config.read(file_path)
    subjects = {}
    for section in config.sections():
        subjects[section] = dict(config.items(section))
    return subjects

# Проверка доступа к объекту с заданными разрешениями
def check_access(subject, object_name, permissions):
    if subject in access_matrix and object_name in access_matrix[subject]:
        object_permissions = access_matrix[subject][object_name]
        for permission in permissions:
            if permission not in object_permissions:
                return False
        return True
    return False

# Проверка наследования разрешений по иерархии ролей
def inherit_permissions(role):
    permissions = set()
    if role in role_hierarchy:
        parent_roles = role_hierarchy[role]
        for parent_role in parent_roles:
            permissions.update(inherit_permissions(parent_role))
            if parent_role in permission_assignments:
                permissions.update(permission_assignments[parent_role])
    if role in permission_assignments:
        permissions.update(permission_assignments[role])
    return permissions

# Загрузка данных из файлов
access_matrix = load_access_matrix('accessMatrix.csv')
object_attributes = load_object_attributes('objects.ini')
subject_attributes = load_subject_attributes('subjects.ini')

# Создание иерархии ролей
role_hierarchy = {
    'owner': [],
    'manager': ['owner'],
    'user': ['manager'],
    'adv:user': ['user'],
    'adv:manager': ['manager']
}

# Назначение разрешений ролям
permission_assignments = {
    'owner': ['111'],
    'manager': ['110'],
    'user': ['100'],
    'adv:user': ['110'],
    'adv:manager': ['110']
}

# Пример использования
subject = 'subject1'
object_name = 'object1'
permissions = ['111', '110']

# Проверка доступа
if check_access(subject, object_name, permissions):
    print(f"Subject '{subject}' has access to object '{object_name}' with permissions {permissions}")
else:
    print(f"Subject '{subject}' does not have access to object '{object_name}' with permissions {permissions}")

# Проверка наследования разрешений
subject_role = 'adv:user'
inherited_permissions = inherit_permissions(subject_role)
print(f"Permissions inherited by role '{subject_role}': {inherited_permissions}")
