import random

NUM_USERS = 100_000

first_names = [
    "Juan", "Maria", "Jose", "Ana", "Luis", "Carmen", "Pedro", "Sofia",
    "Miguel", "Isabella", "Carlos", "Elena", "Andres", "Patricia",
    "Daniel", "Camila", "Rafael", "Lucia", "Fernando", "Valentina",
    "Mark", "John", "Paul", "James", "Michael", "David", "Robert",
    "Mary", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan",
    "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Betty", "Sandra",
    "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Dorothy",
    "Ryan", "Joshua", "Ethan", "Noah", "Liam", "Mason", "Logan",
    "Lucas", "Jackson", "Aiden", "Oliver", "Jacob", "Elijah",
    "William", "James", "Benjamin", "Alexander", "Michael", "Ethan"
]

last_names = [
    "Dela Cruz", "Santos", "Reyes", "Garcia", "Mendoza", "Torres",
    "Flores", "Aquino", "Castro", "Ramos", "Navarro", "Villanueva",
    "Morales", "Gonzales", "Lopez", "Perez", "Gutierrez", "Salazar",
    "Rivera", "Hernandez", "Diaz", "Alvarez", "Romero", "Serrano",
    "Cruz", "Domingo", "Pascual", "Mercado", "Valdez", "Ocampo",
    "Aguilar", "De Guzman", "Bautista", "Velasco", "Ferrer", "Manalo",
    "Tan", "Lim", "Chua", "Cojuangco", "Sy", "Go", "Uy", "Ong",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller",
    "Davis", "Wilson", "Taylor", "Clark", "Lewis", "Walker",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"
]

cities = [
    "Manila", "Quezon City", "Baguio", "Cebu City", "Davao City",
    "Iloilo City", "Cagayan de Oro", "Taguig", "Pasig", "Makati",
    "Bacolod", "General Santos", "Angeles", "Naga", "Tacloban",
    "Butuan", "Zamboanga", "Puerto Princesa", "Dagupan", "San Fernando",
    "Laoag", "Legazpi", "Tuguegarao", "Calamba", "Batangas City",
    "Lipa", "Antipolo", "Malolos", "Balanga", "Olongapo", "Mandaluyong",
    "Marikina", "Valenzuela", "Pasay", "Muntinlupa", "San Juan", "Navotas",
    "Cavite", "Bulacan", "Rizal", "Laguna", "Pampanga",
    "New York", "Los Angeles", "Chicago", "Houston", "Miami",
    "London", "Manchester", "Paris", "Berlin", "Rome",
    "Tokyo", "Osaka", "Seoul", "Beijing", "Bangkok",
    "Singapore", "Sydney", "Melbourne", "Toronto", "Vancouver"
]

with open("data_user.sql", "w", encoding="utf-8") as f:
    for i in range(1, NUM_USERS + 1):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 70)
        city = random.choice(cities)

        f.write(
            f"INSERT INTO Users (UserID, Name, Age, City) "
            f"VALUES ({i}, '{name}', {age}, '{city}');\n"
        )

print("✅ Large realistic dataset generated!")