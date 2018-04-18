import gui.Main as M
import robot.robotono as robot
from  PyQt4 import QtCore, QtGui
import sys

class MainPlugin(object):
    def __init__(self):
        #create gui component
        self.window = M.Main()
        self.window.show()
        #create nao module
        self.robot = robot.Robot()
        #set signals
        self.set_signals()

    #set signals method
    def set_signals(self):
        #connect to blink module on nao controller
        self.window.blinkButton.clicked.connect(self.robot.launch_blink_behavior)
        #connect to stop blink
        self.window.stopBlinkButton.clicked.connect(self.robot.stop_blink_behavior)
        #connect to hello button hte hello module of the robot
        self.window.helloButton.clicked.connect(self.robot.say_hello)
        #connect signals to the first set of Questions
        self.window.set1Q1Button.clicked.connect(self.robot.set1_question1)
        self.window.set1Q2Button.clicked.connect(self.robot.set1_question2)
        self.window.set1Q3Button.clicked.connect(self.robot.set1_question3)
        #connect signals to the first set of answers
        self.window.set1A1Button.clicked.connect(self.robot.set1_answer1)
        self.window.set1A2Button.clicked.connect(self.robot.set1_answer2)
        self.window.set1A3Button.clicked.connect(self.robot.set1_answer3)
        #connect signals to the second set of Questions
        self.window.set2Q1Button.clicked.connect(self.robot.set2_question1)
        self.window.set2Q2Button.clicked.connect(self.robot.set2_question2)
        self.window.set2Q3Button.clicked.connect(self.robot.set2_question3)
        #connect signals to the second set of answers
        self.window.set2A1Button.clicked.connect(self.robot.set2_answer1)
        self.window.set2A2Button.clicked.connect(self.robot.set2_answer2)
        self.window.set2A3Button.clicked.connect(self.robot.set2_answer3)
        #connect signals to the third set of Questions
        self.window.set3Q1Button.clicked.connect(self.robot.set3_question1)
        self.window.set3Q3Button.clicked.connect(self.robot.set3_question3)
        self.window.set3Q2Button.clicked.connect(self.robot.set3_question2)
        #connect signals to the third set of answers
        self.window.set3A1Button.clicked.connect(self.robot.set3_answer1)
        self.window.set3A2Button.clicked.connect(self.robot.set3_answer2)
        self.window.set3A3Button.clicked.connect(self.robot.set3_answer3)
        #connect to say text for module 3: play musicSpeechButton
        self.window.musicSpeechButton.clicked.connect(self.robot.play_music_speech)
        #connect to reproduce music
        self.window.playMusicButton.clicked.connect(self.robot.launch_audio)
        #connect to stop music
        #self.window.stopMusicButton.clicked.connect(self.robot.pause_audio)
        #goodbye module:
        self.window.bye1Button.clicked.connect(self.robot.bye1)
        self.window.bye2Button.clicked.connect(self.robot.bye2)
        self.window.bye3Button.clicked.connect(self.robot.bye3)
        #finish connect to robot shudown
        #self.window.finishButtton.clicked.connect(self.robot.shutdown)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    m = MainPlugin()
    sys.exit(app.exec_())
