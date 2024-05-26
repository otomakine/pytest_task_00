import paramiko
import pytest


def test_permitrootlogon():
    # Данные для подключения к удаленному серверу
    hostname = "172.24.228.253"
    username = "oto"
    password = "1q2w3e$R%T^Y"
    port = 2200

    # Подключение к серверу по SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    # Получение эффективного значения параметра permitrootlogin
    stdin, stdout, stderr = ssh.exec_command("cat /etc/ssh/sshd_config | awk '/PermitRootLogin/ {print $2}' | head -n 1")
    effective_value = stdout.read().decode("utf-8").strip()

    # Сравнение с эталонным значением
    reference_value = "yes"
    test_reference_value = "prohibit-password"
    print(" Результат:")
    error_count = 0
    if effective_value == reference_value:
        print(f"Текущее значение параметра PermitRootLogin: '{effective_value}' совпадает с эталонным '{reference_value}'")
    else:
        print(f"Текущее значение параметра PermitRootLogin: '{effective_value}' не совпадает с эталонным '{reference_value}'")
        error_count += 1

    # Закрытие SSH-соединения
    ssh.close()

    # Падаем если хотя бы 1 параметр не совпадает
    pytest.fail(f"Текущее значение параметра PermitRootLogin не совпадает с эталонным") if error_count > 0 else print("Всё ОК")
