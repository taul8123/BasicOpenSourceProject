student = []


def add_data():
    global student
    student.append([input("학과: "), input("학번: "), input("이름: "),
                    int(input("국어: ")), int(input("영어: ")), int(input("수학: "))])
    summary = 0

    for i in range(3, 6):
        summary += student[-1][i]

    student[-1].append(summary)
    student[-1].append(summary / 3.0)
    if student[-1][-1] >= 95:
        student[-1].append("A+")
    elif student[-1][-1] >= 90:
        student[-1].append("A0")
    elif student[-1][-1] >= 85:
        student[-1].append("B+")
    elif student[-1][-1] >= 80:
        student[-1].append("B0")
    elif student[-1][-1] >= 75:
        student[-1].append("C+")
    elif student[-1][-1] >= 70:
        student[-1].append("C0")
    elif student[-1][-1] >= 65:
        student[-1].append("D+")
    elif student[-1][-1] >= 60:
        student[-1].append("D0")
    else:
        student[-1].append("F")


def search_data():
    global student
    search_student = input("학번 또는 이름 입력: ")
    check = 0
    for i in range(len(student)):
        if student[i][1] == search_student or student[i][2] == search_student:
            print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
            print(student[i])
            check = 1
    if check == 0:
        print("해당학생이 없습니다.")


def delete_data():
    global student
    search_student_number = input("학번: ")
    search_student_name = input("이름: ")
    for i in range(len(student)):
        if student[i][1] == search_student_number and student[i][2] == search_student_name:
            student.pop(i)
            print("삭제되었습니다.")
            return 0
    print("해당 학생이 없습니다.")


def array_data():
    global student
    print("1.학과순 정렬")
    print("2.학번순 정렬")
    menu4 = int(input("메뉴:"))

    if menu4 == 1:
        student = sorted(student, key=lambda student: student[0])
        print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
        for i in range(len(student)):
            print(student[i])

    elif menu4 == 2:
        student = sorted(student, key=lambda student: student[1])
        print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
        for i in range(len(student)):
            print(student[i])

    else:
        print("메뉴확인!!")
            

while True:
    print("1.데이터 추가")
    print("2.데아터 검색")
    print("3.데이터 삭제")
    print("4.데이터 정렬")
    print("0.종료")

    menu = int(input("메뉴: "))

    if menu == 1:
        add_data()

    elif menu == 2:
        search_data()

    elif menu == 3:
        delete_data()

    elif menu == 4:
        array_data()

    elif menu == 0:
        exit()

    else:
        print("메뉴확인!!")




