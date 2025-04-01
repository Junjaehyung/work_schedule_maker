import numpy as np
import random
import data

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
BeforeJobs = ["FrontGate", "BackGate"]
AfterJobs = ["FrontGate", "BackGate", "School inside patrol", "School outside patrol"]

assigned_workers = {day: set() for day in days}

def assign_lunch_before():
    LunchBeforeTimeFrontGateWorker = [[None] * 2 for _ in range(5)]
    LunchBeforeTimeBackGateWorker = [[None] * 2 for _ in range(5)]

    for day_index, day in enumerate(days):
        for job in BeforeJobs:
            workers = data.LunchBeforeWorkIndexed.get(job, {}).get(day, [])

            available_workers = [w for w in workers if w not in assigned_workers[day]]

            if available_workers:
                selected_workers = random.sample(available_workers, min(2, len(available_workers)))

                assigned_workers[day].update(selected_workers)

                if job == "FrontGate":
                    LunchBeforeTimeFrontGateWorker[day_index] = selected_workers
                elif job == "BackGate":
                    LunchBeforeTimeBackGateWorker[day_index] = selected_workers

    return LunchBeforeTimeFrontGateWorker, LunchBeforeTimeBackGateWorker


def assign_lunch_after():
    LunchAfterTimeFrontGateWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeBackGateWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeSchoolInsidePatrolWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeSchoolOutsidePatrolWorker = [[None] * 2 for _ in range(5)]

    for day_index, day in enumerate(days):
        for job in AfterJobs:
            workers = data.LunchAfterWorkIndexed.get(job, {}).get(day, [])

            available_workers = [w for w in workers if w not in assigned_workers[day]]

            if available_workers:
                selected_workers = random.sample(available_workers, min(2, len(available_workers)))

                assigned_workers[day].update(selected_workers)

                if job == "FrontGate":
                    LunchAfterTimeFrontGateWorker[day_index] = selected_workers
                elif job == "BackGate":
                    LunchAfterTimeBackGateWorker[day_index] = selected_workers
                elif job == "School inside patrol":
                    LunchAfterTimeSchoolInsidePatrolWorker[day_index] = selected_workers
                elif job == "School outside patrol":
                    LunchAfterTimeSchoolOutsidePatrolWorker[day_index] = selected_workers

    return (
        LunchAfterTimeFrontGateWorker,
        LunchAfterTimeBackGateWorker,
        LunchAfterTimeSchoolInsidePatrolWorker,
        LunchAfterTimeSchoolOutsidePatrolWorker,
    )

LunchBeforeTimeFrontGateWorker, LunchBeforeTimeBackGateWorker = assign_lunch_before()
LunchAfterTimeFrontGateWorker, LunchAfterTimeBackGateWorker, LunchAfterTimeSchoolInsidePatrolWorker, LunchAfterTimeSchoolOutsidePatrolWorker = assign_lunch_after()

print("\nLunch Before Time Workers (FrontGate):")
for i, day in enumerate(days):
    print(f"{day}: {LunchBeforeTimeFrontGateWorker[i]}")

print("\nLunch Before Time Workers (BackGate):")
for i, day in enumerate(days):
    print(f"{day}: {LunchBeforeTimeBackGateWorker[i]}")

print("\n\n\n------------------------------------------------------------------\n\n\n")

print("\nLunch After Time Workers (FrontGate):")
for i, day in enumerate(days):
    print(f"{day}: {LunchAfterTimeFrontGateWorker[i]}")

print("\nLunch After Time Workers (BackGate):")
for i, day in enumerate(days):
    print(f"{day}: {LunchAfterTimeBackGateWorker[i]}")

print("\nLunch After Time Workers (School Inside Patrol):")
for i, day in enumerate(days):
    print(f"{day}: {LunchAfterTimeSchoolInsidePatrolWorker[i]}")

print("\nLunch After Time Workers (School Outside Patrol):")
for i, day in enumerate(days):
    print(f"{day}: {LunchAfterTimeSchoolOutsidePatrolWorker[i]}")
