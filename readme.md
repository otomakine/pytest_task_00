## Тестовые задания

### Подготовка
- С помощью Hyper-V создал виртуалку, установил из ```iso``` Ubuntu 24 LTS, поднял SSH, изменил порт с ```22``` на ```2200```, проверил подключение через ```ssh user@ip_address```

### Тестовое задание №1
- Текст задания: %hidden%
- Минимальная рабочаая версия: **[tests\test_01_permitrootlogon_min.py](https://github.com/otomakine/pytest_task_00/blob/main/tests/test_01_permitrootlogon_min.py)**

<details><img style="" src="https://github.com/otomakine/pytest_task_00/assets/29117632/3673cae3-a4c8-43bc-a46c-4b4e2b99ec3c">
<summary><img valign="bottom" width="20" height="20" src="https://img.icons8.com/retro/32/image.png" alt="image"/>
  Результат вывода с ошибкой (у меня на Убунте значение PermitRootLogin => 'prohibit-password')</summary></details>

<details><img style="" src="https://github.com/otomakine/pytest_task_00/assets/29117632/c79325b6-a539-47ab-b556-6f31073ac342">
<summary><img valign="bottom" width="20" height="20" src="https://img.icons8.com/retro/32/image.png" alt="image"/>
  Результат вывода если текущее значение совпадает с эталонным</summary></details>

### Тестовое задание №2
- Текст задания: %hidden%
- Минимальная рабочаая версия: **[tests\test_02_pam_pwquality_min.py](https://github.com/otomakine/pytest_task_00/blob/main/tests/test_02_pam_pwquality_min.py)**

<details><img style="" src="https://github.com/otomakine/pytest_task_00/assets/29117632/70e7ef85-7cc3-495c-b143-baaaf715cd5a">
<summary><img valign="bottom" width="20" height="20" src="https://img.icons8.com/retro/32/image.png" alt="image"/>
  Результат вывода с ошибкой (у меня на Убунте все 6 значений не совпадают с эталонными)</summary></details>

<details><img style="" src="https://github.com/otomakine/pytest_task_00/assets/29117632/a4ce7173-8493-41c9-9460-66b684a7796b">
<summary><img valign="bottom" width="20" height="20" src="https://img.icons8.com/retro/32/image.png" alt="image"/>
  Результат вывода когда все 6 значений совпадают с эталонными</summary></details>


### Работа над новой '_plus' версией
- Новый версия теста **[tests\test_01_permitrootlogon_plus.py](https://github.com/otomakine/pytest_task_00/blob/main/tests/test_01_permitrootlogon_plus.py)** короче и использует функции из фикстур
- Переменные для подключения вынесены в **[tests\secrets.py](https://github.com/otomakine/pytest_task_00/blob/main/tests/secrets.py)** (```host, port, username, password```)
- В файл с фикстурами **[tests\conftest.py](https://github.com/otomakine/pytest_task_00/blob/main/tests/conftest.py)** добавлены следующие функции:
  - **```open_ssh```** (открывает SSH сессию в начале сессии)
  - **```close_ssh```** (закрывает SSH сессию в начале сессии)
  - **```execute_ssh_query```** (можно укоротить, исполняет запрос, принимает запрос как параметр)
  - **```check_file_exists```** (можно укоротить, проверяет существование файла, тест падает если файл не найден)
    
<details><img style="" src="https://github.com/otomakine/pytest_task_00/assets/29117632/c88c732c-582b-4a4a-8069-440c275dd44a">
<summary><img valign="bottom" width="20" height="20" src="https://img.icons8.com/retro/32/image.png" alt="image"/>
  Результат вывода <b>check_file_exists</b> файл не найден</summary></details>
- Можно так же рассмотреть случаи когда несколько одинаковых параметров в файле и т.д.
<br><br>
![image](https://github.com/otomakine/pytest_task_00/assets/29117632/59875854-0a4e-4be4-b6d3-fb388b099def)


