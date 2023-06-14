## Это discord-бот, использующий BingAI для поиска!


![GigaBing](https://github.com/WhiteHodok/GigaBing/assets/39564937/cd551292-6de2-47a3-8cdb-2e13ea105765)




## Dependencies 

- Перед использованием бота , создайте виртуальное окружение (без него может откиснуть EdgeGPT из-за старого ворка селениума):

```sh
python -m venv venv
```

- Войдите в него 

```sh
venv\Scripts\activate.bat - windows

source venv/bin/activate - MacOs , Linux
 
```

- Установите библиотеки 

```sh
pip install aiohttp==3.8.4 && EdgeGPT==0.2.1 && discord-py-interactions && asyncio~=3.4.3
```

- Воткните токен своего бота в код (там сами найдёте , как 2 пальца)

## Before using

- Убедитесь что у вас есть VPN страны , где работает Bing и доступ к нему
- У вас есть расширение для вытягивания куки с сайта
- Перейдите на https://www.bing.com/chat , залогиньтесь и перезагрузите страницу
- Скрапните куки через ваше любимое расширение и поместите их в файл cookie.json
- Вы прекрасны !

## Starting 

```sh
py main.py
```
