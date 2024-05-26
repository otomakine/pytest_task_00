import pytest


def test_permitrootlogon(execute_ssh_query, check_file_exists):
    check_file_exists("/etc/ssh/sshd_config")
    effective_value = execute_ssh_query("cat /etc/ssh/sshd_config | awk '/PermitRootLogin/ {print $2}' | head -n 1")
    print(f"\npermitrootlogon_received: {effective_value}")

    # Задаем эталонное значение
    reference_value = "yes"
    reference_value = "prohibit-password"

    # Сравнение с эталонным значением
    print("\nИтоговый результат:")
    error_count = 0
    if effective_value == reference_value:
        print(f"Текущее значение параметра PermitRootLogin: '{effective_value}' совпадает с эталонным '{reference_value}'")
    else:
        print(f"Текущее значение параметра PermitRootLogin: '{effective_value}' не совпадает с эталонным '{reference_value}'")
        error_count += 1

    # Падаем если хотя бы 1 параметр не совпадает
    pytest.fail(f"Текущее значение параметра PermitRootLogin не совпадает с эталонным") if error_count > 0 else print("Всё ОК")
