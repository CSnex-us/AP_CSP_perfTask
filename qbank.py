# ------------------------------------------------------------------------------
#   QUESTION BANK
#       Interface to Question Bank Repository  
#       Provides CRUD operations 
#       Domain Model for Questions
# ------------------------------------------------------------------------------


class QBank:
    def __init__(self):
        self.Id = 1
        self.question = "This is a Question"
        self.answer = "This is the answer"
        self.rating = 900
        self.topic = "Question topic"

    def getId(self):
        print("My id is  " + str(self.Id))


#qBank = [(1,"question 1", "answer 1.1", "answer 1.2"), (2,"question 2", "answer 2.1", "answer 2.2")]
#print(qBank[1][0])


#def qBank():
    # function args: student, topic/standard
    # returns either a single question or a set of questions
    #pass