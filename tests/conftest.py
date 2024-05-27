import pytest
import paramiko
from secrets import *


@pytest.fixture()
def open_ssh(scope="session", autouse=True):
    print("")
    print("fixture_open_ssh: SSH соединение открывается")
    # Данные для подключения к удаленному серверу
    # Берутся из secrets.py

    # Подключение к серверу по SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOSTNAME, PORT, USERNAME, PASSWORD)
    print("fixture_open_ssh: SSH соединение открыто\n")

    return ssh


@pytest.fixture()
def close_ssh(open_ssh, scope="session", autouse=True):
    print("fixture_close_ssh: SSH соединение закрывается")
    ssh = open_ssh
    ssh.close()
    print("fixture_close_ssh: SSH соединение закрыто")


@pytest.fixture()
def check_file_exists(open_ssh):
    ssh = open_ssh

    def _check_file_exists(filename):
        # Получение результата запроса по SSH
        print("")
        print(f"\nfixture_check_file_exists_query : {filename}")
        #stdin, stdout, stderr = ssh.exec_command(f"hostname -i")
        stdin, stdout, stderr = ssh.exec_command(f"if [ -f {filename} ]; then echo '{filename} file exists'; else echo '{filename} file does not exist'; fi;") # {filename}
        query_result = stdout.read().decode("utf-8").strip()
        print(f"fixture_check_file_exists_result: {query_result}")
        if "does not exist" in query_result:
            error_msg = f"\n{"="*92}\n[!!!] Файл '{filename}' не найден, необходимые данные не могут быть считаны.[!!!]\n{"="*92}"
            print(error_msg)
            pytest.fail(error_msg)
        return query_result

    # print(f"fixture.ssh_query._execute_ssh_query.returned: {_execute_ssh_query}")
    return _check_file_exists


@pytest.fixture()
def execute_ssh_query(open_ssh):
    ssh = open_ssh

    def _ssh_query(query):
        # Получение результата запроса по SSH
        print("")
        print(f"fixture_ssh_query : {query}")
        stdin, stdout, stderr = ssh.exec_command(query)
        query_result = stdout.read().decode("utf-8").strip()
        print(f"fixture_ssh_result: {query_result}")
        return query_result

    # print(f"fixture.ssh_query._execute_ssh_query.returned: {_execute_ssh_query}")
    return _ssh_query
