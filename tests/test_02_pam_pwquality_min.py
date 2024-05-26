import paramiko
import pytest


def test_pam_pwquality_min():
    # Данные для подключения к удаленному серверу
    hostname = "172.24.228.253"
    username = "oto"
    password = "1q2w3e$R%T^Y"
    port = 2200

    # Эталонные значения политики PAM
    reference_values = {
        "retry": 6,
        "ucredit": -1,
        "lcredit": -2,
        "dcredit": -3,
        "ocredit": -4,
        "minlen": 5,
    }
    test_reference_values = {
        "retry": 3,
        "ucredit": 0,
        "lcredit": 0,
        "dcredit": 0,
        "ocredit": 0,
        "minlen": 8,
    }

    # Подключение к серверу по SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    # Сравнение значений
    print(" Результат:")
    error_count = 0
    for key, reference_value in reference_values.items():
        stdin, stdout, stderr = ssh.exec_command("cat /etc/security/pwquality.conf | awk '/" + str(key) + "/ { print $4 }' | head -n 1")
        effective_value = stdout.read().decode("utf-8").strip()

        if key not in reference_values:
            print(f"{key} не найдено в текущей политике")
        elif reference_values[key] != int(effective_value):
            print(f"{key}: текущее значение {effective_value} не совпадает с эталонным {reference_values[key]}")
            error_count += 1
        else:
            print(f"{key}: текущее значение {effective_value} совпадает с эталонным {reference_values[key]}")

    # Закрытие SSH-соединения
    ssh.close()

    # Падаем если хотя бы 1 параметр не совпадает
    if error_count > 0:
        error_msg = f"Тест упал: {error_count} текущих параметров не совпало с эталонными значениями"
        print(error_msg)
        pytest.fail(error_msg)
    else:
        print("Все текущие параметры совпали с эталонными. Всё ОК")
