import numpy as np
import random
import data  # data 모듈 가져오기

# ✅ 요일 리스트
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# ✅ Morning 근무자 배정 함수
def assign_morning_workers():
    """
    요일별 Morning 근무자를 랜덤 배정하는 함수
    """
    MorningWorker = [[None] * 4 for _ in range(5)]  # 5일 × 4명 초기화

    for day_index, day in enumerate(days):
        workers = data.MorningWorkerIndexed.get(day, [])  # 해당 요일의 Morning 근무자 목록 가져오기

        if workers:  # 근무자가 존재할 경우만 실행
            selected_workers = random.sample(workers, min(4, len(workers)))  # 4명 랜덤 선택 (근무자가 부족하면 가능한 만큼)
            MorningWorker[day_index] = selected_workers  # 해당 요일의 배정

    return MorningWorker  # 배정된 Morning Worker 리스트 반환

MorningWorker = assign_morning_workers()

print("\nMorning Time Workers (Hall):")
for i, day in enumerate(days):
    print(f"{day}: {MorningWorker[i]}")

print("\n\n\n------------------------------------------------------------------\n\n\n")