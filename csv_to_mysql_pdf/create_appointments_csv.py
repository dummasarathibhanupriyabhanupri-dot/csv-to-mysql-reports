import csv
from datetime import date, timedelta

therapists = [
    ("Dr. Salma", 150),
    ("Dr. Gutturu Keerthi", 112),
    ("Dr. Naveena Yadav", 112),
    ("Dr. Nalagasula Swetha", 109),
    ("Dr. Hemanth", 104),
    ("Dr. Karthik", 101),
    ("Dr. Shahana Shirin CH", 100),
    ("premaleelavathy", 100),
    ("Dr. Ramya M B", 97),
    ("Dr. Grithika", 96),
    ("Dr. Rajmani Gaurav", 93),
    ("Dr. Faraz", 88),
    ("Dr. Vala Naik Ramavath", 84),
    ("Dr. Sethulekshmi S", 81),
    ("Dr. R. Khyati", 80),
    ("Dr. Morajsekar", 66),
    ("Dr. Saranya", 61),
    ("Dr. Sophia", 51),
    ("Dr. Manasa Yalla", 47),
    ("Dr. ISRAR KHAN", 10),
    ("Dr. abid", 8),
    ("Dr. G Keerthana", 4),
]

start_date = date(2024, 1, 1)

with open("data/appointments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "date", "time"])

    for name, count in therapists:
        for i in range(count):
            writer.writerow([name, start_date + timedelta(days=i), "10:00"])

print("appointments.csv created successfully")
