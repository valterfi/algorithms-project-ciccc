import random

# class Account:
    # implements class account here


class Course:
    def __init__(self, name, code, unit):
        self._courseName = name
        self._courseCode = code
        self._courseUnit = unit

    def getCourseName(self):
        return self._courseName

    def getCourseCode(self):
        return self._courseCode

    def getCourseUnit(self):
        return self._courseUnit


class TakenCourse(Course):
    # implements class TakenCourse
    def __init__(self, collegeCourse, semester, grade=0):
        name = collegeCourse.getCourseName()
        code = collegeCourse.getCourseCode()
        unit = collegeCourse.getCourseUnit()
        super().__init__(name, code, unit)

        self._semester = semester
        self._grade = grade

    def printCourse(self):
        print("Course Name: %s || Course Code: %s || Course Unit %d " % (self._courseName, self._courseCode, self._courseUnit))
        self._semester.printSemester()
        print("Grade %d \n" % (self._grade))


class CollegeCourse(Course):
    # implements and complete class CollegeCourse
    def __init__(self, name, code, unit):
        super().__init__(name, code, unit)
        self._courseUnit = unit

    def printCourse(self):
        print("Course Name: %s | Course Code: %s | Course Unit %d \n" % (self._courseName, self._courseCode, self._courseUnit))


class Student:
    # implements class student here
    def __init__(self, studentProfile, admissionYear=2018):
        self._admissionYear = admissionYear
        self._admissionSemester = 1  # Suppose each student starts in semester 1 of the admission year
        self._generalTranscript = GeneralTranscript()
        self._semesterTranscript = CurrentSemesterTranscript()
        self._studentProfile = studentProfile

    def getAdmissionYear(self):
        return self._admissionYear

    def registerCourse(self, collegeCourse, semester, grade=0):

        courseRegistrationYear = semester.getYear()
        courseRegistrationSemester = semester.getSemesterNo()

        course = TakenCourse(collegeCourse, semester, grade)

        if semester.isCurrentSemester():
            self._semesterTranscript.addCourse(course)
            self._generalTranscript.addCourse(course)
        else:
            self._generalTranscript.addCourse(course)

    def getGTranscript(self):
        return self._generalTranscript

    def getSTranscript(self):
        return self._semesterTranscript


class StudentProfile:
    # implements class student here
    def __init__(self, firstName, lastName, gender, country):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.country = country


class Transcript:
    # implements class transcript here
    def __init__(self):
        self._allTakenCourses = []

    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
        # complete this method

    def printTranscript(self):
        for c in self._allTakenCourses:
            c.printCourse()


class GeneralTranscript(Transcript):
    # implements class GeneralTranscript here
    def __init__(self):
        super().__init__()


class CurrentSemesterTranscript(Transcript):
    # implements class CurrentSemesterTranscript here
    def __init__(self):
        super().__init__()


# class Manager:
    # implements class Manager here


class Semester:
    # implements class Semester here
    def __init__(self, semesterNo, year):
        self._semesterNo = semesterNo
        self._year = year
        self._setIfCurrentSemester()

    def getYear(self):
        return self._year

    def getSemesterNo(self):
        return self._semesterNo

    # checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2019, semester = 2
    def _setIfCurrentSemester(self):
        currentSemester = 2
        currentYear = 2019

        if (self._semesterNo == currentSemester) and (self._year == currentYear):
            self._isCurrentSemester = True
        else:
            self._isCurrentSemester = False

    def isCurrentSemester(self):
        return self._isCurrentSemester

    def printSemester(self):
        print("Year: %d Semester%d isCurrent %d" % (self._year, self._semesterNo, self._isCurrentSemester))

# class Menu:
        # implements class Menu here


class Portal:

    # _currentSemester = Semester(2019, 2)  # Static/class property. Suppose the current semester is second semester 2019
    def __init__(self):
        self._collegeCourses = []
        self._registeredStudents = []

    # use this method to register a student
    def registerStudent(self, student):
        self._registeredStudents.append(student)

    def addCourse(self, collegeCourse):
        self._collegeCourses.append(collegeCourse)
    # class this method to add some random courses to a student - You don't need to understand how this method works. Just call it and it will add some courses
    # to the student and to different semesters

    def addRandomCoursesToStudent(self, student):
        for course in self._collegeCourses:
            rand = random.uniform(0, 1)
            admissionYear = student.getAdmissionYear()
            currentSemester = Portal.getCurrentSemester()

            if currentSemester.getYear() == admissionYear:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = currentSemester.getSemesterNo()
            else:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = 2 * (currentSemester.getYear() - admissionYear) + currentSemester.getSemesterNo()

            randomSemster = random.randint(1, numberOfSemesterBetweenCurrentSemesterAndAdmission - 1)

            year = randomSemster // 2
            semesterNo = (randomSemster % 2) + 1
            semester = Semester(semesterNo, student.getAdmissionYear() + year)

            randomGrade = random.randint(30, 100)

            if rand <= .5:
                student.registerCourse(course, semester, randomGrade)

    # static/class method
    def getCurrentSemester():
        currentSemester = Semester(2, 2019)  # Static/class property. Suppose the current semester is second semester 2019
        return currentSemester


class PortalManager:
    def __init__(self):
        self._portal = Portal()

    def createATestPortal(self):

        # create all courses offered
        self._createAllCollegeCourses()
        # self._portal.printAllCollegeCourses()

        # create a sample student
        sampleStudentProfile = StudentProfile("Peter", "Brown", "M", "Canada")
        sampleStudent1 = Student(sampleStudentProfile, 2017)

        # register the sample student
        self._portal.registerStudent(sampleStudent1)

        # add some random courses with grades to the student
        self._portal.addRandomCoursesToStudent(sampleStudent1)

        sampleStudent1.getGTranscript().printTranscript()

    # create college courses
    def _createAllCollegeCourses(self):
        python = CollegeCourse("Python", "CSCI101", 3)
        objectOrientedProgramming = CollegeCourse("Python", "CSCI101", 2)
        problemSolving = CollegeCourse("Problem Solving", "CSCI201", 1)
        projectManagement = CollegeCourse("Project Management", "CSCI202", 3)
        javaProgramming = CollegeCourse("Java Programming", "CSCI301", 3)
        webDevelopment = CollegeCourse("Web Development", "CSCI302", 2)
        androidProgramming = CollegeCourse("Android Programming", "CSCI401", 2)
        iOSApplication = CollegeCourse("iOS Application", "CSCI402", 3)

        self._portal.addCourse(python)
        self._portal.addCourse(objectOrientedProgramming)
        self._portal.addCourse(problemSolving)
        self._portal.addCourse(projectManagement)
        self._portal.addCourse(javaProgramming)
        self._portal.addCourse(webDevelopment)
        self._portal.addCourse(androidProgramming)
        self._portal.addCourse(iOSApplication)


def main():
    portalManager = PortalManager()
    portalManager.createATestPortal()


main()