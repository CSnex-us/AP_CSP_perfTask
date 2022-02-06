# ------------------------------------------------------------------------------
#   QUESTION BANK
#       Interface to Question Bank Repository  
#       Provides CRUD operations 
#       Domain Model for Questions
# ------------------------------------------------------------------------------


class QBank:    # QBank is the Data Structure for all questions
    def __init__(self, Id):
        self.Id = 1
        self.question = "This is a Question"
        self.qType = "Multiple Choice"  # Could be an Enum.
        self.answer = QAnswer.getAnswer()
        self.rating = 900
        self.topic = "Question topic"

    def getId(self):
        print("My id is  " + str(self.Id))



# ------------------------------------------------------------------------------
#   QUESTION ANSWER MODEL
#       Multiple Choice Questions (MCQ) Require Associated Non-Answers.
#           MCQs would be a 'type' selection.
#           MCQs non-answers may have different propensity for selection
#               that would effect the outcome of success on question.
#           MCQs may have a pool of non-answers in addition to correct answer.
# ------------------------------------------------------------------------------
class QAnswer:
    def __init__(self, Id):
        # will need to have GUID for Id on answers set
        self.Id = 1
        self.IsAnswer = True
        self.answer = "This is the answer"


    def getId(self):
        print("My Answer id is  " + str(self.Id))  


#qBank = [(1,"question 1", "answer 1.1", "answer 1.2"), (2,"question 2", "answer 2.1", "answer 2.2")]
#print(qBank[1][0])


#def qBank():
    # function args: student, topic/standard
    # returns either a single question or a set of questions
    #pass