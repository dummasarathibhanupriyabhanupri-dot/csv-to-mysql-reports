from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
import mysql.connector
from db_config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import os

# Create reports folder if not exists
if not os.path.exists("reports"):
    os.makedirs("reports")

# Connect to MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = conn.cursor()

# ✅ CORRECT SQL QUERY (column name is `name`)
query = """
SELECT name, COUNT(*) AS sessions
FROM appointments
GROUP BY name
ORDER BY sessions DESC
"""
cursor.execute(query)

rows = cursor.fetchall()

cursor.close()
conn.close()

# Prepare table data
table_data = [["Therapist", "Sessions"]]
for row in rows:
    table_data.append([row[0], row[1]])

# Create PDF
pdf_path = "reports/therapist_sessions_report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)

table = Table(table_data, colWidths=[320, 120])

# 🎨 TABLE COLORS & STYLE
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [colors.whitesmoke, colors.lightgrey]),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
]))

doc.build([table])

print("✅ PDF report generated successfully")
print("📄 Location:", pdf_path)
