# Инструкция по развертыванию приложения "Site About Travelling"

Этот репозиторий содержит исходный код приложения "Site About Travelling". Ниже приведены инструкции по развертыванию приложения на вашем локальном компьютере.

## Развертывание

1. **Клонирование репозитория:**
   Сначала склонируйте репозиторий с помощью команды `git clone`:
   ```bash
   git clone https://github.com/KatrinKH/site_about_travelling.git
2. **Переход в директорию с проектом:**
    Перейдите в директорию с загруженным проектом:
    ```bash
    cd site_about_travelling
3. **Запуск контейнера Docker:**
    Запустите контейнер Docker с вашим приложением. В этом примере мы предполагаем, что Dockerfile настроен правильно для копирования файла feedback.json внутрь контейнера:
    ```bash
    docker run -p 5000:5000 -v "$(pwd)"/feedback.json:/app/feedback.json site_about_travelling_flask
4. **Доступ к приложению:**
    После успешного запуска контейнера вы сможете получить доступ к вашему приложению, перейдя по адресу http://localhost:5000 в вашем веб-браузере.