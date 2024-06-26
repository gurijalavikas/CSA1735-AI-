% Facts: student(StudentName, TeacherName, SubjectCode).
student('Alice', 'Mr. Smith', 'MATH101').
student('Bob', 'Mrs. Johnson', 'ENG202').
student('Charlie', 'Mr. Smith', 'MATH101').
student('David', 'Ms. Clark', 'SCI303').
student('Eve', 'Mrs. Johnson', 'ENG202').
student('Frank', 'Ms. Clark', 'SCI303').
student('George', 'Mr. White', 'HIS404').
student('Hannah', 'Mr. White', 'HIS404').

% Rule to find all subjects a student is taking.
find_subjects(StudentName, SubjectCode) :-
    student(StudentName, _, SubjectCode).

% Rule to find all students taking a particular subject.
find_students_by_subject(SubjectCode, StudentName) :-
    student(StudentName, _, SubjectCode).

% Rule to find all students taught by a particular teacher.
find_students_by_teacher(TeacherName, StudentName) :-
    student(StudentName, TeacherName, _).

% Rule to find the teacher of a particular student.
find_teacher(StudentName, TeacherName) :-
    student(StudentName, TeacherName, _).

% Rule to find the teacher of a particular subject.
find_teacher_by_subject(SubjectCode, TeacherName) :-
    student(_, TeacherName, SubjectCode).

% Rule to find all subjects taught by a particular teacher.
find_subjects_by_teacher(TeacherName, SubjectCode) :-
    student(_, TeacherName, SubjectCode).
