import random
import os
from time import sleep

class Account:
    # implements class account here

    # The username must be at least 6 characters long.
    # The password must be at least 6 characters and at least one digit character in it.
    def __init__(self, username, password, student):
        self._username = username
        self._password = password
        self._student = student

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password

    def getStudent(self):
        return self._student


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

    def getSemester(self):
        return self._semester

    def printCourse(self):
        print("Course Name: %s || Course Code: %s || Course Unit %d " % (self._courseName, self._courseCode, self._courseUnit))
        self._semester.printSemester()
        print("Grade %d \n" % (self._grade))

    def getCourseGrade(self):
        return self._grade


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

    def getStudentProfile(self):
        return self._studentProfile

    def getAdmissionSemester(self):
        return self._admissionSemester


class StudentProfile:
    # implements class student here
    def __init__(self, studentId, firstName, lastName, gender, address, country, age):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.address = address
        self.country = country
        self.age = age


class Transcript:
    # implements class transcript here
    def __init__(self):
        self._allTakenCourses = []

    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
        # complete this method

    def getCourses(self):
        return self._allTakenCourses

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


class Manager:
    # implements class Manager here
    def __init__(self, firstName, lastName, title):
        self._firstName = firstName
        self._lastName = lastName
        self._title = title

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getTitle(self):
        return self._title


class Semester:
    # implements class Semester here
    def __init__(self, semesterNo, year):
        self._year = year
        self._semesterNo = semesterNo
        self._setIfCurrentSemester()

    def getYear(self):
        return self._year

    def getSemesterNo(self):
        return self._semesterNo

    # checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2020, semester = 1
    def _setIfCurrentSemester(self):
        currentSemester = 1
        currentYear = 2020

        if (self._semesterNo == currentSemester) and (self._year == currentYear):
            self._isCurrentSemester = True
        else:
            self._isCurrentSemester = False

    def isCurrentSemester(self):
        return self._isCurrentSemester

    def calculateSemesterFrom(semesterNo, semesterYear, currentSemester, currentYear):
        #currentSemester = 1
        #currentYear = 2020

        total = (currentYear - semesterYear + 1) * 2
        if (currentSemester == 1):
            total = total - 1
        if (semesterNo == 2):
            total = total - 1

        return total

    def printSemester(self):
        print("Year: %d Semester%d isCurrent %d" % (self._year, self._semesterNo, self._isCurrentSemester))

################ Actions #######################


class Context:

    def __init__(self, portal, accounts, currentAccount, manager):
        self._portal = portal
        self._accounts = accounts
        self._currentAccount = currentAccount
        self._manager = manager

    def getPortal(self):
        return self._portal

    def getAccounts(self):
        return self._accounts

    def getCurrentAccount(self):
        return self._currentAccount

    def getManager(self):
        return self._manager


class Result:
    def __init__(self, isLogin, isExit):
        self._isLogin = isLogin
        self._isExit = isExit

    def isLogin(self):
        return self._isLogin

    def isExit(self):
        return self._isExit

class ActionFactory:

    def getAction(self, option):
        if (option == 1):
            return PrintCertificateAction()
        elif (option == 2):
            return PrintCoursesAction()
        elif (option == 3):
            return PrintTranscriptAction()
        elif (option == 4):
            return PrintGPAAction()
        elif (option == 5):
            return PrintRankingAction()
        elif (option == 6):
            return PrintAvailableCoursesAction()
        elif (option == 7):
            return ListStudentsAction()
        elif (option == 8):
            return ShowProfileAction()
        elif (option == 9):
            return LogoutAction()
        elif (option == 10):
            return ExitAction()
        else:
            return None

# abstrac class represent a action
class Action:

    def execute(self, context):
        raise NotImplementedError

#1
class PrintCertificateAction(Action):

    def execute(self, context):
        os.system('clear')

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        firstName = student.getStudentProfile().firstName
        lastName = student.getStudentProfile().lastName
        studentId = student.getStudentProfile().studentId
        address = student.getStudentProfile().address

        admissionYear = student.getAdmissionYear()
        admissionSemester = student.getAdmissionSemester()

        currentSemester = Semester.calculateSemesterFrom(admissionSemester, admissionYear, 1, 2020)

        allTakenCourses = student.getGTranscript().getCourses()
        numberTakenCourses = len(allTakenCourses)

        manager = context.getManager()

        print("Dear Sir/Madam, ")
        print("")
        print("")
        print("This is to certify that %s %s with student id %s is a student at semester %s at CICCC." % (firstName, lastName, studentId, currentSemester))
        print("He was admitted to our college in %s and has taken %s course(s) so far. Currently he resides at %s." % (admissionYear, numberTakenCourses, address))
        print("")
        print("")
        print("If you have any question, please don’t hesitate to contact us.")
        print("Thanks,")
        print("[Manager: %s %s %s ]" % (manager.getTitle(), manager.getFirstName(), manager.getLastName()))
        print("")
        print("")

        input()
        os.system('clear')

        return Result(True, False)

#2
class PrintCoursesAction(Action):

    def execute(self, context):
        os.system('clear')

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        firstName = student.getStudentProfile().firstName
        lastName = student.getStudentProfile().lastName

        allTakenCourses = student.getGTranscript().getCourses()

        print("Hi %s %s," % (firstName, lastName))
        print("You have taken the following courses so far: ")

        count = 1
        for course in allTakenCourses:

            semesterInformation = ""
            semester = course.getSemester()
            if (semester.isCurrentSemester()):
                semesterInformation = "[Current semester]"

            print("%d) %s: %s %s" % (count, course.getCourseCode(), course.getCourseName(), semesterInformation))
            count = count + 1

        input()
        os.system('clear')

        return Result(True, False)

#3
class PrintTranscriptAction(Action):

        def execute(self, context):

            os.system('clear')

            currentAccount = context.getCurrentAccount()
            student = currentAccount.getStudent()

            firstName = student.getStudentProfile().firstName
            lastName = student.getStudentProfile().lastName

            allGTranscript = student.getGTranscript()

            print("Hi %s %s," % (firstName, lastName))
            print("Here is your general transcript: ")

            self._printCourses(allGTranscript)

            print("")
            print("")
            print("Here is your current semester transcript: ")

            allSTranscript = student.getSTranscript()

            self._printCourses(allSTranscript)

            input()
            os.system('clear')

            return Result(True, False)

        def _printCourses(self, transcript):
            count = 1
            sumUnits = 0
            gradeUnits = 0
            courses = transcript.getCourses()

            for course in courses:
                sumUnits = sumUnits + course.getCourseUnit()
                gradeUnits = gradeUnits + (course.getCourseGrade() * course.getCourseUnit())
                semesterInformation = ""
                semester = course.getSemester()

                if (semester.isCurrentSemester()):
                    semesterInformation = "[Current semester]"

                print("%d) %s: %s %.2f %s" % (count, course.getCourseCode(), course.getCourseName(), course.getCourseGrade(), semesterInformation))
                count = count + 1

            if len(courses) > 0:

                gpa = gradeUnits / sumUnits

                if isinstance(transcript, GeneralTranscript):
                    print("YOUR GPA IS: %.2f" % (gpa))

                elif isinstance(transcript, CurrentSemesterTranscript):
                    print("YOUR Current Semester GPA IS: %.2f" % (gpa))


#4
class PrintGPAAction(Action):
    def execute(self, context):

        os.system('clear')

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        firstName = student.getStudentProfile().firstName
        lastName = student.getStudentProfile().lastName

        allGTranscript = student.getGTranscript()
        overAllGPA = self._calculateGPA(allGTranscript)

        allSTranscript = student.getSTranscript()
        currentSemGPA = self._calculateGPA(allSTranscript)

        print("Hi %s %s," % (firstName, lastName))
        print("Your overall GPA is %.2f" % (overAllGPA))
        print("Your current semester’s GPA is %.2f" % (currentSemGPA))

        input()

        os.system('clear')

        return Result(True, False)

    def _calculateGPA(self, transcript):
        sumUnits = 0
        gradeUnits = 0
        courses = transcript.getCourses()

        for course in courses:
            sumUnits = sumUnits + course.getCourseUnit()
            gradeUnits = gradeUnits + (course.getCourseGrade() * course.getCourseUnit())

        gpa = 0

        if len(courses) > 0:

            gpa = gradeUnits / sumUnits

        return gpa

#5
class PrintRankingAction(Action):

    def execute(self, context):

        os.system('clear')

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        firstName = student.getStudentProfile().firstName
        lastName = student.getStudentProfile().lastName

        allGTranscript = student.getGTranscript()
        overAllGPA = self._calculateGPA(allGTranscript)

        registeredStudents = context.getPortal().getRegisteredStudents() #all students

        rankValue = self._calculateRank(student, registeredStudents)

        print("Hi %s %s," % (firstName, lastName))
        print("Your overall GPA is %.2f and therefore your rank is %d." %(overAllGPA, rankValue))

        input()

        os.system('clear')

        return Result(True, False)

    def _calculateRank(self, currentStudent, registeredStudents):
        #creating dictionary student => grade
        studentGradesDict = {}
        for registeredStudent in registeredStudents :
            allGTranscript = registeredStudent.getGTranscript()
            studentGradesDict[registeredStudent] = self._calculateGPA(allGTranscript)

        rank = {}
        count = 1
        for student in sorted(studentGradesDict, key=studentGradesDict.get, reverse=True):
            rank[student.getStudentProfile().studentId] = count
            count = count + 1
            #print(student.getStudentProfile().firstName, student.getStudentProfile().studentId, studentGradesDict[student])

        #print("")

        return rank[currentStudent.getStudentProfile().studentId]

    def _calculateGPA(self, transcript):
        sumUnits = 0
        gradeUnits = 0
        courses = transcript.getCourses()

        for course in courses:
            sumUnits = sumUnits + course.getCourseUnit()
            gradeUnits = gradeUnits + (course.getCourseGrade() * course.getCourseUnit())

        gpa = 0

        if len(courses) > 0:

            gpa = gradeUnits / sumUnits

        return gpa

#6
class PrintAvailableCoursesAction(Action):
    
    def execute(self, context):

        os.system('clear')

        collegeCourses = context.getPortal().getCollegeCourses() # all courses

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        takenCourses = student.getGTranscript().getCourses() # all taken courses

        admissionYear = student.getAdmissionYear()
        admissionSemester = student.getAdmissionSemester()

        print("The following courses are offered in CICCC College: ")
        #print("")
        #print("admission semester: %d/%d" %(admissionSemester, admissionYear)) 

        count = 1
        for course in collegeCourses:

            checkTakenCourseTuple = self._checkTakenCourse(course, takenCourses)
            isTakenCourse = checkTakenCourseTuple[0]

            courseInformation = "[Not taken]"
            if isTakenCourse :

                currentTakenCourse = checkTakenCourseTuple[1]

                #calculating semester of a taken course
                semesterCourse = currentTakenCourse.getSemester()
                semesterCourseYear = semesterCourse.getYear()
                semesterCourseNo = semesterCourse.getSemesterNo()

                semesterTermCourse = Semester.calculateSemesterFrom(admissionSemester, admissionYear, semesterCourseNo, semesterCourseYear)

                courseInformation = "[Taken at semester " + str(semesterTermCourse) + "]"
                #print("taken semester: %d/%d" %(semesterCourseNo, semesterCourseYear))

            print("%d) %s: %s: %d units %s" %(count, course.getCourseCode(), course.getCourseName(), course.getCourseUnit(), courseInformation))
            #print("")

            count = count + 1

        input()

        os.system('clear')

        return Result(True, False)

    def _checkTakenCourse(self, collegeCourse, takenCourses):
        for takenCourse in takenCourses :
            if collegeCourse.getCourseCode() == takenCourse.getCourseCode() :
                return (True, takenCourse) #is a taken course

        return (False, None) # is not a taken course


#7
class ListStudentsAction(Action):
    def execute(self, context):

        os.system('clear')

        registeredStudents = context.getPortal().getRegisteredStudents()

        print("There are %d students in CICCC College as following:" % (len(registeredStudents)))

        count = 1

        for student in registeredStudents:

            firstName = student.getStudentProfile().firstName
            lastName = student.getStudentProfile().lastName
            studentId = student.getStudentProfile().studentId

            print("%d) %s %s: %d" % (count, firstName, lastName, studentId))

            count = count + 1

        input()

        os.system('clear')

        return Result(True, False)

#8
class ShowProfileAction(Action):
    def execute(self, context):

        os.system('clear')

        currentAccount = context.getCurrentAccount()
        student = currentAccount.getStudent()

        firstName = student.getStudentProfile().firstName
        lastName = student.getStudentProfile().lastName

        studentId = student.getStudentProfile().studentId

        gender = student.getStudentProfile().gender 
        genderWord = ""
        if gender == "M" :
            genderWord = "Male"
        elif gender == "F" :
            genderWord = "Female"
        elif gender == "O" :
            genderWord == "Other"

        address = student.getStudentProfile().address

        country = student.getStudentProfile().country

        age = student.getStudentProfile().age

        admissionYear = student.getAdmissionYear()

        allGTranscript = student.getGTranscript()
        overAllGPA = self._calculateGPA(allGTranscript)

        courses = allGTranscript.getCourses()
        descriptionCourses = []
        for course in courses:

            description = course.getCourseCode() + ": " + course.getCourseName()

            semester = course.getSemester()
            if (semester.isCurrentSemester()):
                description = description + " [Current semester]"

            descriptionCourses.append(description)
        
        separator = ", "
        print("")
        coursesFormated = separator.join(descriptionCourses)

        print("Name: %s %s" %(firstName, lastName))
        print("StudentID: %d" %(studentId))
        print("Gender: %s" %(genderWord))
        print("Address: %s" %(address))
        print("Country of Origin: %s" %(country))
        print("Age: %d" %(age))
        print("Year of Admission: %d" %(admissionYear))
        print("Overall GPA: %.2f" %(overAllGPA))
        print("Courses Taken So far: %s" %(coursesFormated))

        input()

        os.system('clear')

        return Result(True, False)

    def _calculateGPA(self, transcript):
        sumUnits = 0
        gradeUnits = 0
        courses = transcript.getCourses()

        for course in courses:
            sumUnits = sumUnits + course.getCourseUnit()
            gradeUnits = gradeUnits + (course.getCourseGrade() * course.getCourseUnit())

        gpa = 0

        if len(courses) > 0:

            gpa = gradeUnits / sumUnits

        return gpa

#9
class LogoutAction(Action):

    def execute(self, context):
        return Result(False, False)


#10
class ExitAction(Action):
    def execute(self, context):
        return Result(False, True)


################################################


###########VALIDATION##########################


class Validator:

    def checkValidation(self, value):
        raise NotImplementedError

class ValidatorLength(Validator):
    def checkValidation(self, value):
        if len(value) >= 6 :
            return (True, None)
        else:
            return (False, "Input is not valid! It is necessary at least 6 characters!")

class ValidatorPassword(Validator):
    def checkValidation(self, value):

        greaterThanSix = len(value) >= 6
        
        containsDigit = False
        for char in value :
            if char in "1234567890" :
                containsDigit = True

        if greaterThanSix and containsDigit:
            return (True, None)
        else:
            return (False, "Input is not valid! It is necessary at least 6 characters with at least one digit!")

class ValidatorNumber(Validator):
    def checkValidation(self, value):
        if value.isdigit() :
            return (True, None)
        else:
            return (False, "Input is not valid! Input should be a number!")

class ValidatorYear(Validator):
    def checkValidation(self, value):

        if value.isdigit() :
            year = int(value)
            if year < 2020 :
                return (True, None)
            else :
                return (False, "Input is not valid! Input should be less than 2020!")
        else:
            return (False, "Input is not valid! Input should be a number!")


class ValidatorGender(Validator):
     def checkValidation(self, value):
        if value == "M" or value == "F" or value == "O" :
            return (True, None)
        else:
            return (False, "Input is not valid! Input should be [M/F/O]!")

################################################


class Menu:
    # implements class Menu here
    def printMenu(self):
        print("************************************************************")
        print("Select from the options:")
        print("************************************************************")
        print("-[1] Print my enrolment certificate")
        print("-[2] Print my courses")
        print("-[3] Print my transcript")
        print("-[4] Print my GPA")
        print("-[5] Print my ranking among all students in the college")
        print("-[6] List all available courses")
        print("-[7] List all students")
        print("-[8] Show My Profile")
        print("-[9] Logout")
        print("-[10] Exit")
        #print("-[11] Bonus")
        print("************************************************************")
        print("")


class Login:

    def printLogin(self):
        os.system('clear')
        print("************************************************************")
        print("Please enter your account to login:")
        print("************************************************************")
        print("Username:")
        print("Password:")
        print("")
        print("")
        print("")
        print("----------------")
        print("Not registered yet? Type \"Register\" and press enter to start the registration process!")

    def isRegistered(self, username, accounts):
        for account in accounts:
            if account.getUsername() == username:
                return True
        return False

    def login(self, username, password, accounts):
        for account in accounts:
            if (account.getUsername() == username and account.getPassword() == password):
                return (True, account)
        return (False, None)

    def printWrongLogin(self, portal, accounts):
        os.system('clear')
        print("************************************************************")
        print("Your account does not exist. Please try again!")
        print("************************************************************")
        result = input()
        if result == "Register":
            register = Register()
            register.registerNewUser(portal, accounts)


class Register:

    def _printRegister(self):
        os.system('clear')
        print("************************************************************")
        print("Welcome to CICCC College: Please Register")
        print("************************************************************")

    def registerNewUser(self, portal, accounts):
        self._printRegister()
        firstName = input("Please enter your first name: ")
        lastName = input("Please enter your last name: ")
        gender = self._getInputUser("Please enter your gender [M/F/O]: ", ValidatorGender())
        address = input("Please enter your address: ")
        country = input("Please enter your country of origin: ")
        yearAdmission = int(self._getInputUser("Please enter the year of admission: ", ValidatorYear()))
        age = int(self._getInputUser("Please enter your age: ", ValidatorNumber()))
        username = self._getInputUser("Please enter a username [At least 6 characters]: ", ValidatorLength())
        password = self._getInputUser("Please enter a password [At least 6 characters with at least one digit]: ", ValidatorPassword())

        # Creating a new student profile
        studentId = random.randrange(10**7, 10**8)
        studentProfile = StudentProfile(studentId, firstName, lastName, gender, address, country, age)

        # Creating a new student
        student = Student(studentProfile, yearAdmission)

        # Add random courses
        portal.addRandomCoursesToStudent(student)

        # Creating a new account
        account = Account(username, password, student)

        # Registering the new student
        portal.registerStudent(student)

        # Registering the new account
        accounts.append(account)

        print("")
        print("Thanks, your account and profile has been created successfully. Welcome Aboard %s" % (firstName))
        sleep(2)

    def _getInputUser(self, message, validator):
        value  = input(message)
        validationTuple = validator.checkValidation(value)
        isValid = validationTuple[0]
        while not isValid :
            messageError = validationTuple[1]
            print(messageError)
            value = input(message)
            validationTuple = validator.checkValidation(value)
            isValid = validationTuple[0]
        return value


class Portal:

    # _currentSemester = Semester(2020, 1)  # Static/class property. Suppose the current semester is second semester 2019
    def __init__(self):
        self._registeredStudents = []
        self._collegeCourses = []

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
        currentSemester = Semester(1, 2020)  # Static/class property. Suppose the current semester is first semester 2020
        return currentSemester

    # gettint the registered students
    def getRegisteredStudents(self):
        return self._registeredStudents

    def getCollegeCourses(self):
        return self._collegeCourses


class PortalManager:
    def __init__(self):
        self._portal = Portal()
        self._accounts = []
        self._manager = Manager("Alireza", "Davoodi", "Mr.")

    def createATestPortal(self):

        # create all courses offered
        self._createAllCollegeCourses()
        # self._portal.printAllCollegeCourses()

        # create a sample student
        sampleStudentProfile1 = StudentProfile(111111111, "Peter", "Brown", "M", "Broadway Av", "Canada", 25)
        sampleStudent1 = Student(sampleStudentProfile1, 2017)

        sampleStudentProfile2 = StudentProfile(22222222, "Dan", "Vergara", "M", "Broadway Av", "Peru", 25)
        sampleStudent2 = Student(sampleStudentProfile2, 2017)

        sampleStudentProfile3 = StudentProfile(33333333, "Sejin", "Jeong", "F", "Union Street", "South Korea", 25)
        sampleStudent3 = Student(sampleStudentProfile3, 2017)

        sampleStudentProfile4 = StudentProfile(44444444, "Valterfi", "Oliveira", "M", "Forest Groove Dr", "Brazil", 25)
        sampleStudent4 = Student(sampleStudentProfile4, 2019)

        # register the sample student
        self._portal.registerStudent(sampleStudent1)
        self._portal.registerStudent(sampleStudent2)
        self._portal.registerStudent(sampleStudent3)
        self._portal.registerStudent(sampleStudent4)

        # add some random courses with grades to the student
        self._portal.addRandomCoursesToStudent(sampleStudent1)
        self._portal.addRandomCoursesToStudent(sampleStudent2)
        self._portal.addRandomCoursesToStudent(sampleStudent3)
        self._portal.addRandomCoursesToStudent(sampleStudent4)

        # add accounts
        self._accounts.append(Account("peter", "123456", sampleStudent1))
        self._accounts.append(Account("dan", "123456", sampleStudent2))
        self._accounts.append(Account("sejin", "123456", sampleStudent3))
        self._accounts.append(Account("valterfi", "123456", sampleStudent4))

        # sampleStudent1.getGTranscript().printTranscript()
        # print("")
        # sampleStudent1.getGTranscript().printTranscript()
        # print("")
        # sampleStudent1.getGTranscript().printTranscript()
        # print("")
        # sampleStudent1.getGTranscript().printTranscript()
        # sleep(30)

    def startPortal(self):
        isLogin = False

        while(not isLogin):
            os.system('clear')

            login = Login()
            login.printLogin()

            username = input("Username: ")
            if login.isRegistered(username, self._accounts):

                password = input("Password: ")

                resultLogin = login.login(username, password, self._accounts)
                successLogin = resultLogin[0]
                currentAccount = resultLogin[1]
                if (successLogin):
                    os.system('clear')
                    print("************************************************************")
                    print("Welcome to CICCC College!")
                    print("************************************************************")
                    input()

                    isLogin = True

                    os.system('clear')

                    while(isLogin):

                        menu = Menu()
                        menu.printMenu()

                        inputUser = input("Enter the number corresponding to each item to proceed: ")
                        inputIsValid = inputUser.isdigit()

                        while not inputIsValid :
                            print("Invalid Option!")
                            inputUser = input("Enter the number corresponding to each item to proceed: ")
                            inputIsValid = inputUser.isdigit()

                        option = int(inputUser)

                        context = Context(self._portal, self._accounts, currentAccount, self._manager)
                        actionFactory = ActionFactory()
                        action = actionFactory.getAction(option)

                        if action == None :
                            print("Option not found!")
                            sleep(2)
                            os.system('clear')
                            continue

                        result = action.execute(context)

                        if result.isExit():
                            return
                        elif not result.isLogin():
                            isLogin = False

                else:
                    login.printWrongLogin(self._portal, self._accounts)

            else:
                login.printWrongLogin(self._portal, self._accounts)

    # create college courses
    def _createAllCollegeCourses(self):
        python = CollegeCourse("Python", "CSCI101", 3)
        objectOrientedProgramming = CollegeCourse("Object Oriented Programming", "CSCI102", 2)
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
    portalManager.startPortal()


main()
