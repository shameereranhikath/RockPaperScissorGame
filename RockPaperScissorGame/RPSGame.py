import random
from PyQt5 import QtWidgets,uic
HumanScore=0
ComputerScore=0

def number_to_choice(choice):
    return {0:'Rock',1:'Paper',2:'Scissor'}[choice]

def choice_to_number(choice):
    return {'Rock':0,'Paper':1,'Scissor':2}[choice]

def computer_choice():
    return random.choice(["Rock","Paper","Scissor"])

def game_result(CompChoice,HumChoice):
    global HumanScore
    global ComputerScore
    CompChoice_val=choice_to_number(CompChoice)
    HumChoice_val=choice_to_number(HumChoice)
    if HumChoice_val==CompChoice_val:
        dig.label_6.setText("Tie")
    elif (CompChoice_val-HumChoice_val)%3==1:
        dig.label_6.setText("Computer Wins")
        ComputerScore+=1
        dig.label_4.setText(str(ComputerScore))
    else:
        dig.label_6.setText("You Wins")
        HumanScore+=1
        dig.label_3.setText(str(HumanScore))







def set_choice_text_btnRock():
    dig.label_5.setText("Rock")
    Computerchoice=computer_choice()
    dig.label_7.setText(Computerchoice)
    humanchoice="Rock"
    game_result(Computerchoice,humanchoice)


    # dig.label_6.setText(Computerchoice)


def set_choice_text_btnPaper():
    dig.label_5.setText("Paper")
    Computerchoice=computer_choice()
    dig.label_7.setText(Computerchoice)
    humanchoice="Paper"
    game_result(Computerchoice,humanchoice)


def set_choice_text_btnScissor():
    dig.label_5.setText("Scissor")
    Computerchoice=computer_choice()
    dig.label_7.setText(Computerchoice)
    humanchoice="Scissor"
    game_result(Computerchoice,humanchoice)

def set_intial_status_for_labels():
    dig.label_3.setText(str(0))
    dig.label_4.setText(str(0))
    dig.label_5.setText("---")
    dig.label_7.setText("---")
    dig.label_6.setText("---")



app=QtWidgets.QApplication([])
dig=uic.loadUi("RPS.ui")
# dig.setStyleSheet("background-image:url(./img.png)");
set_intial_status_for_labels()
dig.pushButton.clicked.connect(set_choice_text_btnRock)
dig.pushButton_2.clicked.connect(set_choice_text_btnPaper)
dig.pushButton_3.clicked.connect(set_choice_text_btnScissor)
dig.show()
app.exec()





# def computer_choice():

computer_choice=choice_to_number(random.choice(["rock","paper","scissor"]))
print(computer_choice)
print(number_to_choice(1))
print(choice_to_number('scissor'))
