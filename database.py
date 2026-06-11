import sqlite3

conn = sqlite3.connect("prompt.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prompts(
    id INTEGER PRIMARY KEY,
    user_prompt TEXT,
    optimized_prompt TEXT
)
""")

conn.commit()
conn.close()

print("Database Ready")