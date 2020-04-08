class Exam:
    # every class has a constructor, if we declare it, it's called __init__
    # it takes self, you can access self.stuff
    def __init__(self):
        self.multiple_choice = []
        self.true_false = []
        self.short_answer = []

    def add_multiple_choice(self, prompt, options, correct_answer):
        pass

    def add_true_false(self, prompt, t_or_f):
        self.true_false.append([prompt, t_or_f])

    # AI
    def add_short_answer(self, prompt, answer_string):
        self.true_false
        # accesses the instance that called this method, and gets variables from that instance
        self.short_answer

    def give_exam(self):
        for question in self.true_false:
            print(question[0])
            t_or_f = input('Enter True or False')
            while t_or_f.lower() not in ['true', 'false']:
                t_or_f = input('Try again, Enter True or False')
            if t_or_f.lower() == 'true' and question[1] == True:
                print('You are correct.')
            elif t_or_f.lower() == 'false' and question[1] == False:
                print('You are correct.')
            else:
                print('You are not correct.')


# python passes lists as mutable objects, by reference.
# Question is: do classes pass by value, or reference?
#   Does a class, passed into a function get copied, or just renamed as local variable (but still references the original instance)?
#   primitive types int, bool, string, float (immutable, passed by value) these are copied rather than passed as references
#   classes behave more like dictionaries and lists, not copied, passed by reference
def give_exams(student_list, exam_to_give):
    for student in student_list:
        exam_to_give.give_exam()


def modify_exam(some_exam):
    some_exam.add_true_false('Does this modify the original exam?', True)
    print(some_exam.true_false)

# random_exam is what we call an 'instance' of the class
# each instance gets its own internal variables, not shared.
#   gigantic exception : class variables
random_exam = Exam()
random_exam.add_true_false('Is the sky blue?', True)
random_exam.add_true_false('Is the space pope Reptilian?', True)
random_exam.add_true_false('Is three an even number', False)

# random_exam.give_exam()

other_exam = Exam()
print(random_exam.true_false)
modify_exam(random_exam)
# if passed by value, this wouldn't change
# if pass by reference, then this is modified
print(random_exam.true_false)
