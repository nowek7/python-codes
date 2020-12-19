import json
import getpass

try:
    import paramiko
except ImportError error:
    print("Can't import the paramiko package! You must install the paramiko package")

import sys
from typing import Union

PARAMS = frozenset(('user', 'passwd', 'host', 'cert', 'issued_to'))


def help():
    msg = r'''
    How run:

        python some-path\setup-auth-windows.py user=root passwd=root host=127.0.0.1 issued_to=cert_name cert=path\cert_name.crt

    Params:
        user=username (default root)

        passwd=user password

        host=host address (default 127.0.0.1)

        issued_to=for who certificate is issued

        cert=absolute path to certificate

    '''
    print(msg)


def handle_connection(data: dict) -> None:
    user = data.get('user', 'root')
    passwd = data.get('passwd', 'root')
    host = data.get('host', '127.0.0.1')
    port = data.get('port', 22)
    cert = data['cert']
    issued_to = data['issued_to']

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, password=passwd, username=user)
    print(f'Connected to {host}:{port}')

    try:
        replace_certificate(ssh, cert)
        change_controller_serial_json(ssh, issued_to)
        change_user_passw(ssh, user, passwd)
    except Exception as ex:
        raise ex
    finally:
        ssh.close()
        print(f'Connection was closed')


def replace_certificate(ssh: paramiko.SSHClient, cert: str) -> None:
    content = None
    with open(cert) as file:
        content = file.read()

    if not content:
        raise ValueError('Can\'t copy certificate')

    try:
        # Run a command in a running container
        docker_cmd = 'docker exec -t broker-extern sh -c'
        cmd = f'echo "{content}" > /mosquitto/certs/m2m.crt'
        exec_cmd = f'{docker_cmd} {cmd}'
        stdin, stdout, stderr = ssh.exec_command(exec_cmd, get_pty=True)
        check_outputs(stdout, stderr, False)

        print('Certificate changed')
    except Exception as ex:
        raise ex


def change_controller_serial_json(ssh: paramiko.SSHClient,
                                  issued_to: str) -> None:
    try:
        directory = '~/var/lib/docker/volumes/system-manager/_data'
        cmd = f'ls {directory}/ | grep .json'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        file = check_outputs(stdout, stderr)

        cmd = f'cat {directory}/{file}'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        content = check_outputs(stdout, stderr)

        # Replace 'serial' key.
        content = json.loads(content)
        content['serial'] = issued_to
        content = json.dumps(content,  indent=2).strip()

        cmd = f'echo "{content}" > {directory}/{file}'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        check_outputs(stdout, stderr, False)

        print('JSON changed')
    except Exception as ex:
        raise ex


def change_user_passw(ssh: paramiko.SSHClient, user: str, passwd: str) -> bool:
    try:
        do_change = input(f'Can you change password {user} user [y/n]: ')
        if do_change.lower() == 'y':
            new_passwd = getpass.getpass("Set new password for {user}: ")

            cmd = f'echo -e \"{passwd}\n{new_passwd}\n{new_passwd}\"'
            cmd = f'{cmd} | passwd {user}'
            stdin, stdout, stderr = ssh.exec_command(cmd)
            output = check_outputs(stdout, stderr)

            print('Password successfully changed')
    except Exception as ex:
        raise ex


def check_outputs(stdout, stderr, get_output=True) -> Union[str, None]:
    if stderr.channel.recv_stderr_ready():
        error = stderr.channel.recv_stderr(1024).decode('utf8')
        raise ValueError(error)

    output = None
    if get_output:
        try:
            while (len(stdout.channel.in_buffer) == 0):
                return output

            num_bytes = len(stdout.channel.in_buffer)
            output = stdout.read(num_bytes).decode('utf-8')
            output = output.strip()
        except Exception as ex:
            raise ex

    return output


if __name__ == "__main__":
    args = sys.argv[1:]
    data = {}
    try:
        for arg in args:
            param, value = arg.split('=')
            if param in PARAMS:
                data[param] = value
            else:
                print("Unknown parameter!")
                help()
                raise

        handle_connection(data)
    except Exception as ex:
        print(ex)
