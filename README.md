
# FastAPI + PostgreSQL Docker Starter

A Dockerized **FastAPI** application with **PostgreSQL** database, preconfigured with:  
- Automatic database initialization (`init.sql`)  
- PGAdmin for database management (optional)  
- Hot-reload for development  

---

##  Quick Start  

### **Prerequisites**  
- Docker ([Install Guide](https://docs.docker.com/get-docker/))  
- Docker Compose  

### **1. Clone the Repository**  
```bash
git clone https://github.com/pabbico/Project_2_Python_FastAPI_App_with_PostgreSQL.git
cd Project_2_Python_FastAPI_App_with_PostgreSQL
```

### **2. Configure Environment Variables**  
Update .env:  
```ini
# PostgreSQL
DB_PASSWORD=your_secure_password
DB_NAME=fastapi_db
DB_USER=postgres

# PGAdmin (optional)
PGADMIN_EMAIL=admin@example.com
PGADMIN_PASSWORD=admin_password

# FastAPI
APP_PORT=8000
```

### **3. Start the Services**  
```bash
docker-compose up -d
```

---

## Access Services
| Service | URL | Credentials |  
|---------|-----|------------|  
| **FastAPI** | http://localhost:8000 | - |  
| **PGAdmin** | http://localhost:5050 | Email: `admin@example.com`<br>Password: `admin_password` |  
| **PostgreSQL** | `db:5432` | Username: `postgres`<br>Password: `your_secure_password` |  

---

## **🔍 Project Structure**  
```bash
fastapi-postgres-docker/
├── .env                    # Environment variables
├── docker-compose.yml      # Defines services
├── db/
│   └── init.sql            # Database schema + seed data
└── app/
    ├── main.py             # FastAPI application
    └── requirements.txt    # Python dependencies
```

---

##  Development  

### **Key Features**  
- **Auto-init Database**: Tables created on startup via `init.sql`.  
- **Hot-Reload**: Code changes trigger live updates.  
- **Persistent Data**: PostgreSQL volume retains data between restarts.  

### **Endpoints**  
| Route | Method | Description |  
|-------|--------|-------------|  
| `/` | `GET` | Hello message |  
| `/items/` | `GET` | List all items |  

---

##  Docker Commands  
| Command | Description |  
|---------|-------------|  
| `docker-compose up -d` | Start all services |  
| `docker-compose down` | Stop all services |  
| `docker-compose logs -f web` | View FastAPI logs |  
| `docker exec -it fastapi-postgres-db-1 psql -U postgres` | Access PostgreSQL shell |  

---

##  Troubleshooting
### **PGAdmin Connection**  
1. Add a new server in PGAdmin:  
   - **Host**: `db` (Docker service name)  
   - **Username**: `postgres`  
   - **Password**: From `.env`  

##  License
MIT License. See [LICENSE](LICENSE).  

---

##  Credits  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)  

---
