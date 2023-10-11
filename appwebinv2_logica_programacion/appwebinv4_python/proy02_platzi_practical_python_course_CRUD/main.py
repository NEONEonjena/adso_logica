import sys

clients = [
    {
        'name' : 'pablo',
        'company' : 'google',
        'email' : 'pablo@google.com',
        'position' : 'software enginner',
    },
    {
        'name' : 'ricardo',
        'company' : 'facebook',
        'email' : 'ricardo@facebook.com',
        'position' : 'data science enginner',
    }
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')
        

def list_clients():
    print('-' * 82)
    print('id | name\t| company\t| email\t\t\t| position\t\t |')
    print('-' * 82)
    for idx, client in enumerate(clients):
        print(' {uid} | {name} \t| {company} \t| {email} \t| {position}\t |'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))
    print('-' * 82)


def update_client(client_id, update_client):
    global clients

    if len(clients) - 1 >= client_id:        
        clients[client_id] = update_client
    else:
        print()
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message='What is the client {}?: '):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print()


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()
    print()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        print()
        list_clients()
    elif command == 'L':
        list_clients()    
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        print()
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        print()

        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        print()
        if found:
            print('The client is in our client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')


print()