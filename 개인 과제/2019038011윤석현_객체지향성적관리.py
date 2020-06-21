class student :

    def __init__(self):
        self.new_student = []


    def add_data(self):
        self.new_student.append(input("학과: "))
        self.new_student.append(input("학번: "))
        self.new_student.append(input("이름: "))
        self.new_student.append(int(input("국어: ")))
        self.new_student.append(int(input("영어: ")))
        self.new_student.append(int(input("수학: ")))
        summary = 0

        for i in range(3, 6):
            summary += self.new_student[i]

        self.new_student.append(summary)
        self.new_student.append(summary / 3.0)
        if self.new_student[-1] >= 95:
            self.new_student.append("A+")
        elif self.new_student[-1] >= 90:
            self.new_student.append("A0")
        elif self.new_student[-1] >= 85:
            self.new_student.append("B+")
        elif self.new_student[-1] >= 80:
            self.new_student.append("B0")
        elif self.new_student[-1] >= 75:
            self.new_student.append("C+")
        elif self.new_student[-1] >= 70:
            self.new_student.append("C0")
        elif self.new_student[-1] >= 65:
            self.new_student.append("D+")
        elif self.new_student[-1] >= 60:
            self.new_student.append("D0")
        else:
            self.new_student.append("F")

        return self.new_student



def search_data():
    search_student = input("학번 또는 이름 입력: ")
    check = 0
    for i in range(len(student_list)):
        if student_list[i][1] == search_student or student_list[i][2] == search_student:
            print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
            print(student_list[i])
            check = 1
    if check == 0:
        print("해당학생이 없습니다.")

def delete_data():
    search_student_number = input("학번: ")
    search_student_name = input("이름: ")
    for i in range(len(student_list)):
        if student_list[i][1] == search_student_number and student_list[i][2] == search_student_name:
            student_list.pop(i)
            print("삭제되었습니다.")
            return 0
    print("해당 학생이 없습니다.")

def array_data():
    print("1.학과순 정렬")
    print("2.학번순 정렬")
    menu4 = int(input("메뉴:"))

    if menu4 == 1:
        student_list.sort(key=lambda student_list: student_list[0])
        print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
        for i in range(len(student_list)):
            print(student_list[i])

    elif menu4 == 2:
        student_list.sort(key=lambda student_list: student_list[1])
        print("['학과', '학번', '이름', 국어성적, 영어성적, 수학성적, 총점, 평균, '학점']")
        for i in range(len(student_list)):
            print(student_list[i])

    else:
        print("메뉴확인!!")

student_list = []

while True:
    print("1.데이터 추가")
    print("2.데아터 검색")
    print("3.데이터 삭제")
    print("4.데이터 정렬")
    print("0.종료")

    menu = int(input("메뉴: "))

    if menu == 1:
        new_student = student()
        student_list.append(new_student.add_data())

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


