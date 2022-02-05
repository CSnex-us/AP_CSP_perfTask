# ------------------------------------------------------------------------------
#   Answer BANK
#       Interface to Answer Bank Repository  
#       Provides CRUD operations for Answers Associated with Question(s) 
#       Domain Model for Answers
# ------------------------------------------------------------------------------


class ABank:    # ABank is the Data Structure for all answers
    def __init__(self, qId, qType):
        # will need to have GUID for Id on answers set
        self.Id = 10
        self.IsAnswer = True
        self.answer = "This is the answer"

    def getAnswer(self, qId, ):
        print("My id is  " + str(self.Id))
        # may return set of answers if is MCQ or TFQ
        # may return Unit Test if Question is Code Execution Question (CEQ)



# ------------------------------------------------------------------------------
#   QUESTION / ANSWER MODEL
#       Multiple Choice Questions (MCQ) Require Associated Non-Answers.
#           MCQs would be a 'type' selection.
#           MCQs non-answers may have different propensity for selection
#               that would effect the outcome of success on question.
#           MCQs may have a pool of non-answers in addition to correct answer.
# ------------------------------------------------------------------------------
