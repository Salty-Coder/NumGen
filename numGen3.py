import random
import time
import tracemalloc
import colorama

tracemalloc.start()
colorama.init()


option = int(input("Option: "))

#----------------------------------------------------------------------
def Opt1():

    starter = int(input("Start Number: "))
    ender = int(input("End Number: "))
    find = int(input("Find: "))
    delay = float(input("Delay: "))
    delay = int(delay)
    show = int(input("1: Show numbers. 2: Dont show: "))
    tries = 0
    print("---------------------------")
    startTime = time.time()
    while True:
        time.sleep(delay)
        num = random.randint(starter, ender)
        if show == 1:
            print(num)
        tries = tries + 1
        if num == find:
            break
    current, peak = tracemalloc.get_traced_memory()
    endTime = time.time()
    hours, rem = divmod(endTime - startTime, 3600)
    minutes, seconds = divmod(rem, 60)
    seconds = round(seconds, 4)
    print(colorama.Fore.GREEN + "Found " + str(find) + " after " + str(tries) + " tries with the scale " + str(starter) + "-" + str(ender) + ". " + colorama.Fore.RESET + "Performed in " + str(hours) + "h, " + str(minutes) + "m, " + str(seconds) + "s with the delay of " + str(delay) + " seconds. " + colorama.Fore.RED + "\nThe peak memory usage was " + str(peak / 10**6) + "MB" + colorama.Fore.RESET)
    tracemalloc.stop()

#----------------------------------------------------------------------


#----------------------------------------------------------------------
def Opt2():

    starter = int(input("Start Number: "))
    ender = int(input("End Number: "))
    find = int(input("Find: "))
    repeats = int(input("Repeats: "))
    repeat = 0
    delay = float(input("Delay: "))
    delay = int(delay)
    show = int(input("1: Show numbers. 2: Dont show: "))
    tries = 0
    print("---------------------------")
    startTime = time.time()
    while repeat < repeats:
        repeat = repeat + 1
        while True:
            time.sleep(delay)
            num = random.randint(starter, ender)
            if show == 1:
                print(num)
            tries = tries + 1
            if num == find:
                break
    current, peak = tracemalloc.get_traced_memory()
    endTime = time.time()
    hours, rem = divmod(endTime - startTime, 3600)
    minutes, seconds = divmod(rem, 60)
    seconds = round(seconds,4)
    print(colorama.Fore.GREEN + "Found " + str(find) + " after an average of " + str(tries / repeats) + " tries (" + str(repeats) +" Repeats) with the scale " + str(starter) + "-" + str(ender) + ". "  + colorama.Fore.RESET + "Performed in " + str(hours) + "h, " + str(minutes) + "m, " + str(seconds) + "s with the delay of " + str(delay) + " seconds. " + colorama.Fore.RED + "\nThe peak memory usage was " + str(peak / 10**6) + "MB" + colorama.Fore.RESET)
    tracemalloc.stop()

#----------------------------------------------------------------------

if option == 1:
    Opt1()
if option == 2:
    Opt2()