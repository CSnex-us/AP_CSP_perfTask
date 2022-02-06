'''
    Question Bank Server
    Based on matching Student Profiency and Question Difficulty
'''
from qbank import QBank

print("Hello AP CSC Perfomrance Task Project")

studentId = int(input("Enter your student Id: "))
numQuestions = int(input("Enter how many questions do you want to generate: "))

question1 = QBank()
print(question1.Id)
print(question1.getId())

# TODO  Create DataSet:  a) Students  b) Question Bank
#           student: name, progress  

# TODO  Statistical Range of 70% Success Rate

# TODO  How to connect answer to question
#           def getQuestion(student, standard):
#           choose appropriate question
#            

