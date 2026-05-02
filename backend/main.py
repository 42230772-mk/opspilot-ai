from fastapi import FastAPI
import mysql.connector
import requests

app = FastAPI()


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="opspilot_ai"
    )


@app.get("/")
def read_root():
    return {"message": "OpsPilot AI Backend is running"}


@app.get("/health/db")
def check_database_connection():
    try:
        connection = get_db_connection()
        connection.close()
        return {"status": "success", "message": "Connected to MySQL database"}
    except Exception as error:
        return {"status": "error", "message": str(error)}
    
    
@app.get("/leads")
def get_leads():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM leads
        WHERE status NOT IN ('won', 'lost')
        ORDER BY
            CASE interest_level
                WHEN 'high' THEN 1
                WHEN 'medium' THEN 2
                WHEN 'low' THEN 3
            END,
            next_followup_date ASC
    """)

    leads = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "count": len(leads),
        "leads": leads
    }
    
    
@app.get("/tasks")
def get_tasks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE status != 'completed'
        ORDER BY
            CASE priority
                WHEN 'high' THEN 1
                WHEN 'medium' THEN 2
                WHEN 'low' THEN 3
            END,
            due_date ASC
    """)

    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "count": len(tasks),
        "tasks": tasks
    }
    
    
@app.get("/operations/summary-data")
def get_summary_data():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM leads
        WHERE status NOT IN ('won', 'lost')
        ORDER BY
            CASE interest_level
                WHEN 'high' THEN 1
                WHEN 'medium' THEN 2
                WHEN 'low' THEN 3
            END,
            next_followup_date ASC
    """)
    leads = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE status != 'completed'
        ORDER BY
            CASE priority
                WHEN 'high' THEN 1
                WHEN 'medium' THEN 2
                WHEN 'low' THEN 3
            END,
            due_date ASC
    """)
    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    optimized_leads = [
        {
            "name": lead["name"],
            "company": lead["company"],
            "interest_level": lead["interest_level"],
            "next_followup_date": lead["next_followup_date"],
            "status": lead["status"]
        }
        for lead in leads
    ]
    
    optimized_tasks = [
        {
            "title": task["title"],
            "priority": task["priority"],
            "due_date": task["due_date"],
            "status": task["status"]
        }
        for task in tasks
    ]
    
    return {
        "leads_count": len(optimized_leads),
        "tasks_count": len(optimized_tasks),
        "leads": optimized_leads,
        "tasks": optimized_tasks
    }
    
    
@app.get("/briefings")
def get_briefings():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM briefing_logs
        ORDER BY briefing_date DESC
        LIMIT 10
    """)

    briefings = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "count": len(briefings),
        "briefings": briefings
    }
    
    
@app.post("/trigger-briefing")
def trigger_briefing():
    try:
        response = requests.post(
            "http://localhost:5678/webhook/trigger-briefing"
        )

        return {
            "status": "success",
            "n8n_response": response.text
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }