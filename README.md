# Task API

A small CRUD API for managing a to-do list — create, read, update, and delete tasks — built with **Python** and **FastAPI** as part of the FlyRank AI Internship, Backend Track, Week 2.

Data is stored **in-memory** (a Python list) — there's no database yet, so all tasks reset when the server restarts. That's intentional for this stage of the assignment, not a bug.

## Run it

```bash
git clone https://github.com/YOUR-USERNAME/flyrank-crud-api.git
cd flyrank-crud-api
python -m venv venv
venv\Scripts\Activate.ps1        # Windows PowerShell
pip install -r requirements.txt
uvicorn main:app --reload
```

The server runs at **http://localhost:8000**
Interactive Swagger docs at **http://localhost:8000/docs**

## Endpoints

| Method | Path          | Description                        | Status codes         |
|--------|---------------|-------------------------------------|------------------------|
| GET    | `/`           | API info                             | 200                    |
| GET    | `/health`     | Health check                          | 200                    |
| GET    | `/tasks`      | List all tasks                         | 200                    |
| GET    | `/tasks/{id}` | Get a single task                       | 200, 404               |
| POST   | `/tasks`      | Create a new task                        | 201, 400               |
| PUT    | `/tasks/{id}` | Update a task's title and/or done status  | 200, 400, 404          |
| DELETE | `/tasks/{id}` | Delete a task                              | 204, 404               |

## Example request

<!-- Paste a real `curl -i` output here once you've built the endpoints, e.g.: -->

```
$ curl.exe -i http://localhost:8000/tasks/1

HTTP/1.1 200 OK
content-type: application/json

{"id":1,"title":"Buy milk","done":false}
```

## Swagger UI

<img width="1366" height="768" alt="Swagger  Result" src="https://github.com/user-attachments/assets/8edd2540-d871-444b-9800-a84586bf68fa" />

<img width="1366" height="768" alt="Swagger UI 2" src="https://github.com/user-attachments/assets/fa57a2c9-468d-45d1-9381-bac7c81a5899" />

<img width="1354" height="764" alt="Screenshot of crud app in browser" src="https://github.com/user-attachments/assets/c0d6e3b7-22ee-44be-ba6e-2d4429bfba24" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/daea827b-12af-4aca-9194-7d326bfdea88" />


## Notes

<!-- Optional: if you do the "mortality experiment" extra, write your two sentences here about
     what happens to your tasks after restarting the server, and why. -->

## AI vs me

<!-- Fill this in only if/when you do Stage 7 (the bonus AI rematch). Include your full prompt
     and at least three concrete differences you found between your hand-built version and the AI's. -->
