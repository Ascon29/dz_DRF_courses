## Проект приложения lms-системы

---

Описание проекта

---
### Инструкция по запуску проекта:

1. При первом запуске
   - Установить и запустить Docker на ваш компьютер по ссылке [Docker](https://www.docker.com/)
   - Клонировать репозиторий [Github](https://github.com/Ascon29/dz_DRF_courses)
   - Выполнить команду `docker-compose up -d --build`

2. При следующих запусках
   - Выполнить команду `docker-compose up -d`
3. Для остановки проекта
   - Выполнить команду `docker-compose down`

При успешном запуске проекта в терминале появится следующее сообщение:

 ✔ Service web                             Built<br />
 ✔ Service celery-beat                     Built<br />
 ✔ Service celery                          Built<br />
 ✔ Network dz_drf_courses_default          Created<br />
 ✔ Container dz_drf_courses-db-1           Started<br />
 ✔ Container dz_drf_courses-redis-1        Started<br />
 ✔ Container dz_drf_courses-web-1          Started<br />
 ✔ Container dz_drf_courses-celery-1       Started<br />
 ✔ Container dz_drf_courses-celery-beat-1  Started<br />

---