# coding=utf-8
####################################################################################################
##                                 ONO INTERFACE
## Copyright (C) 2017 UFES.
##
## This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
## 
## Maintainers: Andres Ramirez
##              Carolina Carvalho
##
## Laboratorio de Automacao Inteligente - LAI 4
####################################################################################################

#!/usr/bin/python

import time
import logging
import os.path
import uuid
import urllib
import requests
import threading

####################################################################################################
class Robot(object):
    def __init__(self, settings = { 'IpRobot': "192.168.42.1",
                                    'port'   : 9559,
                                    'name'   : 'Palin',
                                    'UseSpanish': True
                                    }
                 ):
        #load settings
        self.settings = settings
        #create Session
        self.s = requests.Session()
        #connect the session to the robot
        self.payload = {'password': 'opsoro123'}
        self.r = self.s.post('http://'+ self.settings['IpRobot'] +'/login/', data=self.payload)
        r_token = self.s.get('http://'+ self.settings['IpRobot'] +'/sockjstoken') 
        self.token_com = r_token.text
        print(self.token_com)
        #demo modules
    def fala(self,value_rph = 1555, value_rpv = 1660, value_lph = 1460, value_lpv = 1600, audio = "", prompt_1 = 2, prompt_2 = 8):
        payload = {'pin_number': 3, 'value': '%d' %value_rph} #value_rph
        r_eye = self.s.get('http://192.168.42.1/robot/servo/', data=payload)
        payload = {'pin_number': 2, 'value': '%d' %value_rpv} #value_rpv
        r_eye = self.s.get('http://192.168.42.1/robot/servo/', data=payload)
        payload = {'pin_number': 13, 'value': '%d' %value_lph} #value_lph
        r_eye = self.s.get('http://192.168.42.1/robot/servo/', data=payload)
        payload = {'pin_number': 10, 'value': '%d' %value_lpv} #value_lpv
        r_eye = self.s.get('http://192.168.42.1/robot/servo/', data=payload)
        payload_s = {'s': '%s' %audio}
        r_sound = self.s.get('http://192.168.42.1/robot/sound/', params=payload_s)
        time.sleep(0.5)
        payload = {'channel': 0, 'pos': 1500, 'prompt': '%d' %prompt_1}
        r_arm = self.s.post('http://192.168.42.1/robot/arm/', data=payload)
        payload = {'channel': 0, 'pos': 1500, 'prompt': '%d' %prompt_2}
        r_arm = self.s.post('http://192.168.42.1/robot/arm/', data=payload)
    def som(self,audio):
        payload_s = {'s': '%s' %audio}
        r_sound = self.s.get('http://192.168.42.1/robot/sound/', params=payload_s)
    def emotion(self,phi):
        payload = {'r': 1.0, 'phi': '%f' %phi, 'time': -1.0}
        r_emo = self.s.post('http://192.168.42.1/robot/emotion/', data=payload)
    #run eyes behavior
    def run_blink_behavior(self):
        #self.behavior_manager.runBehavior("eyes_nao-92db4f/blink_eyes")
        r_app = self.s.get('http://192.168.42.1/openapp/circumplex')
    #run behavior from a separate
    def launch_blink_behavior(self):
        threading.Thread(target = self.run_blink_behavior).start()
    #stop blink behavior
    def stop_blink_behavior(self):
        #self.behavior_manager.stopBehavior("eyes_nao-92db4f/blink_eyes")
        r_clapp = self.s.get('http://192.168.42.1/closeapp')
    #say hello
    def say_hello(self):
        self.fala(1824,1851,1860,1500,"hello.wav")
   #set1 question 1
    def set1_question1(self):
        self.fala(1824, 1851, 1860, 1500, "set1_question1.wav")
    #set1 question 2
    def set1_question2(self):
        self.fala(1824, 1851, 1860, 1500, "set1_question2.wav")
    #set1 question 3
    def set1_question3(self):
        self.fala(1824, 1851, 1860, 1500, "set1_question3.wav")

    ###################################################
    #set2 question 1
    def set2_question1(self):
        self.fala(1824, 1851, 1860, 1500, "set2_question1.wav")
    #set2 question 2
    def set2_question2(self):
        self.fala(1824, 1851, 1860, 1500, "set2_question2.wav")
    #set2 question 3
    def set2_question3(self):
        self.fala(1824, 1851, 1860, 1500, "set2_question3.wav")

    ##################################################
    #set3 question 1
    def set3_question1(self):
        self.fala(1824, 1851, 1860, 1500, "set3_question1.wav")
    #set3 question 2
    def set3_question2(self):
        self.fala(1824, 1851, 1860, 1500, "set3_question2.wav")
    #set3 question 3
    def set3_question3(self):
        self.fala(1824, 1851, 1860, 1500, "set3_question3.wav")

    ############################answers##################
    #set1 answer1
    def set1_answer1(self):
        self.fala(1824, 1851, 1860, 1500, "set1_answer1.wav")

    #set1 answer2
    def set1_answer2(self):
        self.fala(1824, 1851, 1860, 1500, "set1_answer2.wav")
    #set1 answer2
    def set1_answer3(self):
        self.fala(1824, 1851, 1860, 1500, "set1_answer3.wav")
    #################################################
    #set2 answer1
    def set2_answer1(self):
        self.fala(1824, 1851, 1860, 1500, "set2_answer1.wav")

    #set2 answer2
    def set2_answer2(self):
        self.fala(1824, 1851, 1860, 1500, "set2_answer2.wav")
    #set2 answer2
    def set2_answer3(self):
        self.fala(1824, 1851, 1860, 1500, "set2_answer3.wav")
    ################################################
    #set3 answer1
    def set3_answer1(self):
        self.fala(1824, 1851, 1860, 1500, "set3_answer1.wav")
    #set3 answer2
    def set3_answer2(self):
        self.fala(1824, 1851, 1860, 1500, "set3_answer2.wav")
    #set3 answer2
    def set3_answer3(self):
        self.fala(1824, 1851, 1860, 1500, "set3_answer3.wav")

    ################################################
    def play_music_speech(self):
        self.som("play_music_speech.wav")

    def launch_audio(self):
        threading.Thread(target = self.play_audio).start()

    def play_audio(self):
        self.som("cancion.wav")
        
    def bye1(self):
        #self.tts.say("Eso fue todo por hoy")
        self.fala(1824, 1851, 1860, 1500, "bye1.wav")

    def bye2(self):
        #self.tts.say("Gracias por venir")
        self.fala(1824, 1851, 1860, 1500, "bye2.wav")

    def bye3(self):
        #self.tts.say("Hasta luego")
        self.fala(1824, 1851, 1860, 1500, "bye3.wav")
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
