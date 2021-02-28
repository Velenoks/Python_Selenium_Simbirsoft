# Python_Selenium_Simbirsoft
<h2>Тесты для gmail.com</h2>

В данном тесте выполняются следующие действия:
1) С помощью Selenium открыть браузер, открыть gmail.com, авторизоваться, зайти на
почту;
2) С помощью Selenium определить, сколько нашлось писем от пользователя с электронным адресом;
3) С помощью Selenium и интерфейса почты автоматически написать и отправить
письмо пользователю, в тексте которого указать найденное в шаге 2
количество писем. Указать тему письма "Тестовое задание. <Фамилия>", где
<Фамилия> - это Ваша фамилия;

<h2>Развертывание окружения</h2>

Чтобы развернуть окружжение Selenium Grid, необходиом выполнить команду <code>docker-compose -p grid up --force-recreate</code>, дождитесь полного запуска контейнеров, после этого можете приступать к тестам.

<h2>Переменные в файле .env</h2>

Обязательно, перед началом тестирования, проверьте переменные окружения в файле <b>.env</b><br>
<b>EMAIL</b> - ваша электронная почта от gmail<br>
<b>PASSWORD</b> - ваш пароль от <b>EMAIL</b><br>
<b>TO_EMAIL</b> - электронная почта которую вы хотите протестировать<br>

<h2>Отчеты Allure</h2>

Для создания отчетов Allure вам необходимо при запуске тестов добавить <code>--allurediv results</code>, где <b>results</b> директория, куда будут сохранены отчеты.

<h2>Запуск тестов</h2>

Для запуска тестов необходимо выполнить команду <code>pytest --driver Remote --capability browserNam
e firefox --alluredir results</code>, где <b>firefox</b> - это бразер через которые производиться запуск. Из коробки есть Firefox и Chrome.

<h2>Локальный запуск тестов</h2>

Чтобы запустить тесты локально, нужно выполнить команду <code>pytest --driver Firefox --alluredir results</code> - для Firefox и <code>pytest --driver Chrome --alluredir results</code> - для Chrome. Но без драйверо они не запустяться, поэтому их необходимо скачать и расположить в дериктории проекта. Ссылка для <a href=https://sites.google.com/a/chromium.org/chromedriver/downloads>ChromeDriver</a> и для <a href=https://github.com/mozilla/geckodriver/releases>Firefox</a>

<h2>Установленные пакеты</h2>

1. pytest 
2. selenium
3. pytest-selenium 
4. python-dotenv 
5. allure-pytest 
