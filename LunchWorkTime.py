import numpy as np
import random
import data  # data 모듈 가져오기

# 요일 및 업무 리스트
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
BeforeJobs = ["FrontGate", "BackGate"]
AfterJobs = ["FrontGate", "BackGate", "School inside patrol", "School outside patrol"]

# ✅ 중복 방지: 요일별 배정된 근무자를 저장할 딕셔너리
assigned_workers = {day: set() for day in days}

# ✅ 점심 전 근무자 배정 함수
def assign_lunch_before():
    LunchBeforeTimeFrontGateWorker = [[None] * 2 for _ in range(5)]
    LunchBeforeTimeBackGateWorker = [[None] * 2 for _ in range(5)]

    for day_index, day in enumerate(days):
        for job in BeforeJobs:  # "FrontGate", "BackGate"
            workers = data.LunchBeforeWorkIndexed.get(job, {}).get(day, [])  # 해당 요일의 근무자 목록 가져오기

            # 중복 방지를 위해 필터링
            available_workers = [w for w in workers if w not in assigned_workers[day]]

            if available_workers:  # 근무자가 존재할 경우만 실행
                selected_workers = random.sample(available_workers, min(2, len(available_workers)))  # 2명 랜덤 선택

                # 배정된 근무자 기록 (중복 방지)
                assigned_workers[day].update(selected_workers)

                if job == "FrontGate":
                    LunchBeforeTimeFrontGateWorker[day_index] = selected_workers
                elif job == "BackGate":
                    LunchBeforeTimeBackGateWorker[day_index] = selected_workers

    return LunchBeforeTimeFrontGateWorker, LunchBeforeTimeBackGateWorker


# ✅ 점심 후 근무자 배정 함수
def assign_lunch_after():
    LunchAfterTimeFrontGateWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeBackGateWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeSchoolInsidePatrolWorker = [[None] * 2 for _ in range(5)]
    LunchAfterTimeSchoolOutsidePatrolWorker = [[None] * 2 for _ in range(5)]

    for day_index, day in enumerate(days):
        for job in AfterJobs:  # "FrontGate", "BackGate", "School inside patrol", "School outside patrol"
            workers = data.LunchAfterWorkIndexed.get(job, {}).get(day, [])  # 해당 요일의 근무자 목록 가져오기

            # 중복 방지를 위해 필터링
            available_workers = [w for w in workers if w not in assigned_workers[day]]

            if available_workers:  # 근무자가 존재할 경우만 실행
                selected_workers = random.sample(available_workers, min(2, len(available_workers)))  # 2명 랜덤 선택

                # 배정된 근무자 기록 (중복 방지)
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


# ✅ 함수 실행
LunchBeforeTimeFrontGateWorker, LunchBeforeTimeBackGateWorker = assign_lunch_before()
LunchAfterTimeFrontGateWorker, LunchAfterTimeBackGateWorker, LunchAfterTimeSchoolInsidePatrolWorker, LunchAfterTimeSchoolOutsidePatrolWorker = assign_lunch_after()



# ✅ 결과 출력
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
