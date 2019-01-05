#!python3

import random, os

# States and their capitals
capitals = {
                'Andhra Pradesh'    : 'Hyderabad',
                'Arunachal Pradesh' : 'Itanagar',
                'Assam'             : 'Dispur',
                'Bihar'             : 'Patna',
                'Chhattisgarh'      : 'Raipur',
                'Goa'               : 'Panaji',
                'Gujrat'            : 'Gandhinagar',
                'Haryana'           : 'Chandigarh',
                'Himachal Pradesh'  : 'Shimla',
                'Jammu and Kashmir' : 'Srinagar',
                'Jharkhand'         : 'Ranchi',
                'Karnataka'         : 'Bengaluru',
                'Kerela'            : 'Thiruvananthapuram',
                'Madhya Pradesh'    : 'Bhopal',
                'Maharashtra'       : 'Mumbai',
                'Manipur'           : 'Imphal',
                'Meghalaya'         : 'Shillong',
                'Mizoram'           : 'Aizawl',
                'Nagaland'          : 'Kohima',
                'Odisha'            : 'Bhubaneswar',
                'Punjab'            : 'Chandigarh',
                'Rajasthan'         : 'Jaipur',
                'Sikkim'            : 'Gangtok',
                'Tamil Nadu'        : 'Chennai',
                'Telangana'         : 'Hyderabad',
                'Tripura'           : 'Agartala',
                'Uttar Pradesh'     : 'Lucknow',
                'Uttrakhand'        : 'Dehradun',
                'West Bengal'       : 'Kolkata'
            }
# Create a folder to store quiz files
os.makedirs('.\\CapitalQuiz')
os.chdir('.\\CapitalQuiz')
# Generate 50 quiz files

for quizNum in range(50):
    
    quizFileName = 'capitalsQuiz'+str(quizNum+1)+'.txt'
    answerKeyFileName = 'capitalsQuiz_answerKey'+str(quizNum+1)+'.txt'
    
    quizFile = open(quizFileName,'w')
    answerKey = open(answerKeyFileName,'w')

    quizFile.write((' '*20)+'STATE-CAPITAL QUIZ (Form No. {0})\n'.format(quizNum+1))
    
    quizFile.write('Name :\nRoll No. :\nDate :\n')
    quizFile.write('\n')

    # Shuffle states
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(29):

        # Write questions in quizFile
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('{0}. What is the capital of {1}?\n'.format(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write(['(A)','(B)','(C)','(D)'][i]+' '+answerOptions[i]+'\n')
        quizFile.write('\n')

        # Write correct answer in answerKey
        answerKey.write('{0}. {1}\n'.format(questionNum+1,correctAnswer))

    quizFile.close()
    answerKey.close()
