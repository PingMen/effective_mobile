# Test Job — Flask + Nginx Infrastructure

## 📦 Описание проекта

Проект состоит из двух сервисов:

- `backend` — Flask-приложение на Python
- `nginx` — reverse proxy сервер

Nginx принимает HTTP-запросы на порт `80`
и проксирует их в backend-сервис.

---

## 🚀 Используемые технологии

- Python 3.12
- Flask
- Docker
- Docker Compose
- Nginx

---

# 📂 Структура проекта

```bash
.
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
└── docker-compose.yml
```

---

# ⚙️ Пошаговая инструкция запуска

## 1. Клонировать репозиторий

```bash
git clone <repository_url>
cd <project_name>
```

---

## 2. Запустить проект

```bash
docker compose -f docker-compose.yml up -d
```

---

## 3. Проверить запущенные контейнеры

```bash
docker ps
```

Ожидаемый результат:

- backend
- nginx

---

# ✅ Проверка работоспособности

## Проверка через браузер

Открыть:

```text
http://localhost
```

---

## Проверка через curl

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

---

# 🏗 Архитектура проекта

## Схема взаимодействия

```text
              HTTP :80
+-----------+ -------------> +-----------+
|   Client  |                |   Nginx   |
+-----------+ <------------- +-----------+
                                   |
                                   |
                                   | proxy_pass
                                   v
                           +----------------+
                           | Flask Backend  |
                           |  backend:8080  |
                           +----------------+
```

---

# 🔄 Как работает схема nginx → backend

1. Пользователь отправляет HTTP-запрос на порт `80`

2. Запрос попадает в контейнер `nginx`

3. Nginx перенаправляет запрос в backend:

```nginx
proxy_pass http://backend:8080;
```

4. Flask-приложение обрабатывает запрос

5. Ответ возвращается через Nginx клиенту

---

# 🐳 Docker Compose

Контейнеры находятся в одной Docker-сети.

Nginx обращается к backend по имени сервиса:

```text
backend:8080
```

Docker DNS автоматически резолвит имя контейнера.

---
