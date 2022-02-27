# If else

# 학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.
# # 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.
#
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
# print_grade 함수는 파라미터로 중간고사 점수 midterm_score와 기말고사 점수 final_score를 받고, 최종 성적을 출력합니다.

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score

    if (total > 90):
        print("A")
    elif (total >= 80):
        print("B")
    elif (total >= 70):
        print("C")
    elif (total >= 60):
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)


# B를 받기 위해서는 총 점수가 '80점 이상이면서 90점 미만'이어야 하는데
# 위에 작성된 조건을 보면 80 <= total < 90이 아니라 그냥 total >= 80임
# elif문으로 넘어 왔다는 것은 앞선 if문의 조건 부분을 통과하지 않았다는 뜻이므로 점수가 90점 미만일 수밖에 없다는 것!