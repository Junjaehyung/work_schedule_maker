import numpy as np
import random
import data

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

def assign_morning_workers():
    MorningWorker = [[None] * 2 for _ in range(5)]

    for day_index, day in enumerate(days):
        workers = data.MorningWorkerIndexed.get(day, [])

        if workers:
            selected_workers = random.sample(workers, min(4, len(workers)))
            MorningWorker[day_index] = selected_workers

    return MorningWorker

MorningWorker = assign_morning_workers()

print("\nMorning Time Workers (Hall):")
for i, day in enumerate(days):
    print(f"{day}: {MorningWorker[i]}")

print("\n\n\n------------------------------------------------------------------\n\n\n")