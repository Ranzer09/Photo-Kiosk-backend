# Photo Kiosk Backend

A FastAPI-based backend for user management with JWT authentication, using PostgreSQL and SQLAlchemy.

## Features

- User CRUD operations (create, read, update, delete).
- JWT-based authentication with PyJWT.
- PostgreSQL database managed via pgAdmin.
- Environment variable configuration with `.env`.

## Prerequisites

- **Python 3.12**: [python.org](https://www.python.org/downloads/)
- **PostgreSQL 15+**: [postgresql.org](https://www.postgresql.org/download/)
- **pgAdmin 4**: [pgadmin.org](https://www.pgadmin.org/download/)
- **Git**: [git-scm.com](https://git-scm.com/) (optional)
- **Command Prompt/Terminal**

## Setup Instructions

### 1. Clone or Download

git clone <repository-url>
cd photo-kiosk-backend

### 2. Set Up Virtual Environment

cd \photo-kiosk-backend
python -m venv myenv
myenv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

If missing, install manually:
pip install fastapi uvicorn sqlalchemy psycopg2-binary pyjwt passlib[bcrypt] python-dotenv

### 4. Configure PostgreSQL with pgAdmin

1. **Install PostgreSQL**:
   - Set password for `postgres` user (e.g., `admin`).
   - Verify port `5432`:
    cmd
     netstat -aon | findstr 5432
    

2. **Install pgAdmin**:
   - Open pgAdmin and register a server:
     - Name: `Local PostgreSQL`
     - Host: `localhost`
     - Port: `5432`
     - Username: `postgres`
     - Password: `admin`

3. **Create Database**:
   - Right-click **Databases** > **Create** > **Database**.
   - Name: `photo-kiosk`
   - Owner: `postgres`

4. **Create `users` Table**:
   - In `photo-kiosk` database, open **Query Tool**.
   - Run:
    sql
     CREATE TABLE users (
         userid SERIAL PRIMARY KEY,
         username VARCHAR(255) NOT NULL UNIQUE,
         password VARCHAR(255) NOT NULL,
         role VARCHAR(255) NOT NULL,
         createdAt DATE NOT NULL DEFAULT CURRENT_DATE
     );
    

### 5. Configure Environment Variables

Create `.env`:
echo SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(32))") > .env
echo SQLALCHEMY_DATABASE_URL=postgresql://postgres:admin@localhost:5432/photo-kiosk >> .env

### 6. Run the Application

uvicorn main:app --reload

Access at `http://localhost:8000`.

### 7. Test Endpoints

  Using postman,

- **Create User**:
POST
Url: "http://localhost:8000/users" 
- Body:
{
  "username":"test",
  "password":"1234",
  "role":"Photographer"
}


- **Login**:
POST 
Url: "http://localhost:8000/users" 
- Body:
{
  "username":"test",
  "password":"1234",
}



- **Get User**:
GET
Url:"http://localhost:8000/users/1"


- **Delete User**:
DELETE
Url:"http://localhost:8000/users/1"


### Troubleshooting

- **Database Errors**: Verify `SQLALCHEMY_DATABASE_URL` and PostgreSQL service.
- **Dependency Issues**: Reinstall dependencies or check `pip list`.
- **JWT Errors**: Ensure `SECRET_KEY` is set in `.env`.
