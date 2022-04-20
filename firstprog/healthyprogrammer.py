#
# from pygame import mixer
# from time import time
#
# def music_play(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.set_volume(1)
#     mixer.music.play()
#     while True:
#         user_input = input()
#         if user_input == stopper:
#             mixer.music.stop()
#             break
#
#
# def log_time(msg):
#     import time
#     named_tuple = time.localtime()
#     time_string = time.strftime("%d/%m/%y at %H:%M:%S", named_tuple)
#
#     f = open("log.txt","a")
#     f.write(f"{msg} on {time_string} \n")
#
# watersec = 40*60
# eyesec = 30*60
# physec = 45*60
# initial_water = time()
# init_eye = time()
# init_phy = time()
#
# while True:
#     if time() - initial_water > watersec:
#         print("it's time to drink water, enter drank to stop")
#         music_play("Bismillah.mp3","drank")
#         initial_time = time()
#         log_time("drank water")
#
#     if time() - init_eye > eyesec:
#         print("it's time to relax eyes, enter eydone to stop")
#         music_play("Bismillah.mp3", "eydone")
#         initial_time = time()
#         log_time("eyes relaxed")
#
#     if time() - init_phy > physec:
#         print("it's time to exercise, enter exdone to stop")
#         music_play("Bismillah.mp3", "exdone")
#         initial_time = time()
#         log_time("done exercise")

# from pygame import mixer
# import time
#
# named_tuple = time.localtime()
# time_string = time.strftime("%d/%m/%y at %H:%M:%S", named_tuple)

# from time import time
#
#
#
#
#
# initial_water = time()
# init_eye = time()
# init_phy = time()
#
# while True:
#     if time() - initial_water > 5:
#         print("it's time to drink water, enter drank to stop")
#         mixer.init()
#         mixer.music.load("Bismillah.mp3")
#         mixer.music.play()
#         user_input = input()
#         if user_input == "drank":
#             mixer.music.stop()
#         f = open("log.txt","a")
#         f.write(f"drank water {time_string} \n")
#         initial_water = time()






