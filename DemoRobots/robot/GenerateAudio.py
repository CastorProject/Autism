# coding=utf-8
# audio generation file #
import qi
import sys
import threading


import robot

r = robot.Robot()
r.tts.sayToFile("Hola \\pau=300\\ mi nombre es Ono!", '/tmp/audio/hello.wav')

#set1 q1######################################################
r.tts.sayToFile("Cuál es tu nombre?", '/tmp/audio/set1_question1.wav')

r.tts.sayToFile("Cuántos anios tienes!", '/tmp/audio/set1_question2.wav')

r.tts.sayToFile("Te gusta jugar?", '/tmp/audio/set1_question3.wav')
#set2 q2###############################################################
r.tts.sayToFile("Cuál es tu color favorito?", '/tmp/audio/set2_question1.wav')

r.tts.sayToFile("Cuántos hermanos tienes", '/tmp/audio/set2_question2.wav')

r.tts.sayToFile("Te gusta ir al colegio?", '/tmp/audio/set2_question3.wav')
#set3 q #############################################################
r.tts.sayToFile("Cuál es tu comida favorita?", '/tmp/audio/set3_question1.wav')

r.tts.sayToFile("Cuántos ojos tienes?", '/tmp/audio/set3_question2.wav')

r.tts.sayToFile("Te gusta la música?", '/tmp/audio/set3_question3.wav')

#set1 answers###########################################################
r.tts.sayToFile("Mucho gusto!", '/tmp/audio/set1_answer1.wav')

r.tts.sayToFile("yo tengo dos anios", '/tmp/audio/set1_answer2.wav')

r.tts.sayToFile("A mi me encanta jugar", '/tmp/audio/set1_answer3.wav')

#set 2 answers######################################################

r.tts.sayToFile("El mío es el rojo!", '/tmp/audio/set2_answer1.wav')

r.tts.sayToFile("yo tengo dos hermanos", '/tmp/audio/set2_answer2.wav')

r.tts.sayToFile("A mi me gusta mucho el colegio", '/tmp/audio/set2_answer3.wav')
#set3 answers#######################################################
r.tts.sayToFile("La mía es la pasta!", '/tmp/audio/set3_answer1.wav')

r.tts.sayToFile("yo tengo dos ojos", '/tmp/audio/set3_answer2.wav')

r.tts.sayToFile("A mi me encanta la música", '/tmp/audio/set3_answer3.wav')

#######################################################
r.tts.sayToFile("Canta conmigo ésta canción", '/tmp/audio/play_music_speech.wav')

###bye1
r.tts.sayToFile("Eso fue todo por hoy", '/tmp/audio/bye1.wav')
r.tts.sayToFile("Gracias por venir", '/tmp/audio/bye2.wav')
r.tts.sayToFile("Hasta luego", '/tmp/audio/bye3.wav')
