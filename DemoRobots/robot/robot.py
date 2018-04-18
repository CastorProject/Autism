# coding=utf-8
"""ROBOT CODE"""
import qi
import sys
import threading


class Robot(object):
    def __init__(self, settings = { 'IpRobot': "192.168.0.102",
                                    'port'   : 9559,
                                    'name'   : 'Palin',
                                    'UseSpanish': True
                                    }
                 ):
        #load settings
        self.settings = settings

        #create Session
        self.session = qi.Session()
        #connect the session to the robot
        #self.connect_session()
        self.session.connect("tcp://" + self.settings['IpRobot'] + ":" + str(self.settings['port']))
        #after connecting to the robot, get services and modules
        self.get_services()



    #connect to the robot through session
    """def connect_session(self):
        try:
            self.session.connect("tcp://" + self.settings['IpRobot'] + ":" + str(self.settings['port']))
        except RuntimeError:
            logging.debug("Can't connect to Naoqi at ip \"" + self.settings['IpRobot'] + "\" on port " + str(self.settings['port'] +".\n"
                          "Please check your script arguments. Run with -h option for help.")
    """

    #get all module services
    def get_services(self):
        #text to speech module service
        self.tts = self.session.service("ALTextToSpeech")
        #set language
        self.setLanguage('Spanish')
        #animated text to speech service
        self.animatedSpeech = self.session.service("ALAnimatedSpeech")
        #motion service
        self.motion = self.session.service("ALMotion")
        #posture service
        self.posture = self.session.service("ALRobotPosture")
        #leds module
        self.leds = self.session.service("ALLeds")
        #audio module
        self.audio = self.session.service("ALAudioPlayer")
        #behavior manager
        self.behavior_manager = self.session.service("ALBehaviorManager")

    #demo modules

    #run eyes behavior
    def run_blink_behavior(self):
        self.behavior_manager.runBehavior("eyes_nao-92db4f/blink_eyes")
    #run behavior from a separate
    def launch_blink_behavior(self):
        threading.Thread(target = self.run_blink_behavior).start()
    #stop blink behavior
    def stop_blink_behavior(self):
        self.behavior_manager.stopBehavior("eyes_nao-92db4f/blink_eyes")

    #say hello
    def say_hello(self):
        self.motion.wakeUp()
        self.tts.say("Hola \\pau=300\\ mi nombre es Jánsel!")

    #set1 question 1
    def set1_question1(self):
        self.tts.say("Cuál es tu nombre?")
    #set1 question 2
    def set1_question2(self):
        self.tts.say("Cuántos anios tienes")
    #set1 question 3
    def set1_question3(self):
        self.tts.say("Te gusta jugar?")

    ###################################################
    #set2 question 1
    def set2_question1(self):
        self.tts.say("Cuál es tu color favorito?")
    #set2 question 2
    def set2_question2(self):
        self.tts.say("Cuántos hermanos tienes")
    #set2 question 3
    def set2_question3(self):
        self.tts.say("Te gusta ir al colegio?")

    ##################################################
    #set3 question 1
    def set3_question1(self):
        self.tts.say("Cuál es tu comida favorita?")
    #set3 question 2
    def set3_question2(self):
        self.tts.say("Cuántos ojos tienes?")
    #set3 question 3
    def set3_question3(self):
        self.tts.say("Te gusta la música?")

    ############################answers##################
    #set1 answer1
    def set1_answer1(self):
        self.tts.say("Mucho gusto!")

    #set1 answer2
    def set1_answer2(self):
        self.tts.say("yo tengo dos anios")
    #set1 answer2
    def set1_answer3(self):
        self.tts.say("A mi me encanta jugar")
    #################################################
    #set2 answer1
    def set2_answer1(self):
        self.tts.say("El mío es el rojo!")

    #set2 answer2
    def set2_answer2(self):
        self.tts.say("yo tengo dos hermanos")
    #set2 answer2
    def set2_answer3(self):
        self.tts.say("A mi me gusta mucho el colegio")
    ################################################
    #set3 answer1
    def set3_answer1(self):
        self.tts.say("La mía es la pasta!")

    #set3 answer2
    def set3_answer2(self):
        self.tts.say("yo tengo dos ojos")
    #set3 answer2
    def set3_answer3(self):
        self.tts.say("A mi me encanta la música")

    ################################################
    def play_music_speech(self):
        self.tts.say("Canta conmigo ésta canción")

    def launch_audio(self):
        threading.Thread(target = self.play_audio).start()

    def play_audio(self):
        self.auid = self.audio.playFile("/home/nao/cancion.wav")


    def pause_audio(self):
        self.audio.stopAll()

    ###############################################
    def bye1(self):
        self.tts.say("Eso fue todo por hoy")

    def bye2(self):
        self.tts.say("Gracias por venir")

    def bye3(self):
        self.tts.say("Hasta luego")

    #set language method
    def setLanguage(self, value):
        self.tts.setLanguage(value)

    def shutdown(self):
        self.motion.rest()

    #load Dialogs
    #TODO: LOAD Dialogs from files
    def load_dialogs(self):
        print("look in the database to load available dialogs")

if __name__ == '__main__':
    r = Robot()
    r.say_hello()
    r.set1_question1()
    r.set1_question2()
    r.set1_question3()

    r.set2_question1()
    r.set2_question2()
    r.set2_question3()

    r.set3_question1()
    r.set3_question2()
    r.set3_question3()

    r.set1_answer1()
    r.set1_answer2()
    r.set1_answer3()

    r.set2_answer1()
    r.set2_answer2()
    r.set2_answer3()

    r.set3_answer1()
    r.set3_answer2()
    r.set3_answer3()

    r.play_music_speech()
    r.play_audio()

    r.bye1()
    r.bye2()
    r.bye3()

    r.shutdown()
