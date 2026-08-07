# Infrastructure Monitoring Service

проект, демонстрирующий полный цикл разработки и развертывания backend-сервиса

Цель проекта — построить production-like окружение с использованием современных инструментов:

- автоматическая сборка приложения;
- контейнеризация;
- CI pipeline;
- публикация Docker-образов;
- оркестрация через Kubernetes;
- подготовка мониторинга приложения.

---

# Используемый стек

## Backend

- Python
- FastAPI
- REST API

## Контейнеризация

- Docker
- Docker Compose
- Docker Hub

## CI/CD

- GitHub Actions (CI)

## Kubernetes

- k3s
- Kubernetes Deployment
- Kubernetes Service
- Kubernetes Ingress
- Traefik

## Мониторинг

- Prometheus metrics endpoint (`/metrics`)

---

# Реализованный функционал

## FastAPI REST API

Создан backend-сервис на FastAPI.

Реализовано:

- REST API;
- структура приложения;
- запуск приложения в контейнере;
- endpoint для сбора метрик.

Доступный endpoint мониторинга: GET /metrics


Endpoint возвращает метрики в формате, совместимом с Prometheus.

---

# Docker

Приложение полностью контейнеризировано.

Реализовано:

- Dockerfile;
- сборка Docker-образа приложения;
- запуск приложения внутри контейнера;
- воспроизводимое окружение.

Схема работы:

Исходный код
|
v
Docker build
|
v
Docker image
|
v
Docker container

---

# Docker Compose

Добавлена локальная оркестрация через Docker Compose.

Позволяет запускать приложение в локальной среде одной командой:

```bash
docker compose up
```
## Continuous Integration

Настроен CI pipeline через GitHub Actions.

Реализовано:

- автоматический запуск workflow при изменении репозитория;
- проверка сборки проекта;
- подготовка Docker-образа.

### Pipeline:

GitHub Repository
        |
        v
 GitHub Actions
        |
        v
 Build & Checks

## Docker Hub

Настроена интеграция с Docker Hub.

### Реализованный процесс:

Изменение кода
       |
       v
GitHub Actions
       |
       v
Сборка Docker image
       |
       v
Публикация в Docker Hub

Docker-образ может использоваться для дальнейшего деплоя в Kubernetes.


## Kubernetes Deployment

Приложение развернуто в Kubernetes-кластере на базе k3s.
Используются следующие Kubernetes-ресурсы:

### Deployment

Deployment отвечает за управление состоянием приложения.
Реализовано:

- запуск Pod с приложением;
- управление состоянием контейнера;
- возможность дальнейшего масштабирования.

## Service

Создан Kubernetes Service.
Назначение:
- стабильный доступ к Pod;
- внутренняя маршрутизация запросов;
- абстракция над сетевым взаимодействием контейнеров.

### Ingress
Настроен внешний доступ к приложению через Kubernetes Ingress.
Используется:

- Ingress Resource;
- Traefik Ingress Controller.

Схема обработки запроса:

Пользователь
      |
      v
 Traefik Ingress
      |
      v
 Kubernetes Service
      |
      v
 FastAPI Pod

Добавлен endpoint метрик приложения: **/metrics**
Он подготовлен для подключения к Prometheus.


## Prometheus + Grafana

На текущий момент реализован только endpoint метрик приложения.
Необходимо добавить полноценный стек мониторинга:
- развертывание Prometheus в Kubernetes;
- настройку сбора метрик;
- подключение ServiceMonitor;
- развертывание Grafana;
- создание dashboard для визуализации состояния приложения.
