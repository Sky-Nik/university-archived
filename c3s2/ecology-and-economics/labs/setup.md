## Технічні пререквізити

Лабораторні роботи нашого курсу можна виконувати на `Maple` та на `Python`. 

Чисто теоретично, інші мови програмування та системи комп'ютерної алгебри не забороняються, але ми маємо великі сумніви у доцільності виконання лабораторних робіт нашого курсу на/у них.

### Python

Рекомендуємо встановити дистрибутив Анаконда доступний до завантаження за посиланнями:

- для [Windows](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe)
- для [macOS](https://repo.anaconda.com/archive/Anaconda3-2018.12-MacOSX-x86_64.pkg)
- для [Linux](https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh)

По ідеї всі необхідні вам для виконання всіх лабораторних робіт пакети все є у цьому дистрибутиві, але якщо ні то нові можна поставити виконавши `bash` команду
```bash
pip install --user package_name
```
або
```bash
pip install --user --upgrade package_name==version_number
```
якщо вам потрібна якась конкретна версія пакету.

Підключенння потрібного пакету у виконуваний файл відбувається одним з наступних рядків:
```python
import package_name
from package_name import function_name
from package_name import *  # import everything from a package
```

Вашу програму на `python`  можна виконати `bash`-командою
```bash
python program_name.py
```
або
```bash
program_name.py
```
якщо ви використовуєте так званий шебанг, тобто якщо перший рядок файлу з вашою програмою має вигляд 
```python
#!/usr/bin/env python
```

### Maple

Із системою комп'ютерної алгебри Maple ви вже маєте бути знайомі з відповідного предмету, що читається на другому курсі.