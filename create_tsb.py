##import time
from TSB import *

start = input('\n To open TSB, hit enter, type tsb(), and hit enter again: \n\n')

def tsb():
    welcome = 'Welcome to TSB -- a place to build tool systems. \n'
    instr = '(Hit enter to continue) [x to skip intro] \n'
    a = 'Think of something you want to create.'
    b = 'What *types* of tools do you need to make it happen?'
    c = 'Say, you want to create a film. You would need recording devices, funding sources, storytelling skills, etc.'
    d = 'Each of these *types* of tools performs a specific function: Recording, Funding, Storytelling.'
    e = "So, we can call them by their function: 'recording tools', 'storytelling tools', etc. \nNow, let's define these functions a little further:"
    g = 'For example, \nRecording = the preservation of visual/auditory data in digital form,'
    h = 'Funding = the procurement of money for the purchase of necessary materials and services.'
    i = 'Often, tools interact:'
    j = 'One might need funding to attain recording tools. \nThe tools of storytelling will (hopefully) guide recording. \nSometimes, the limitations of recording and funding limits storytelling.'
    m = 'Looking at the ways tools interact can sometimes give surprising and *useful* insights.'
    n = 'Think again of that thing you want to create.'
    o = 'Think of the types of tools you need.'
    p = 'Below is a set of tools meant to help you -- organize and explore *your* system of tools.'
    q = 'Tip: call tools by their function (e.g. Backscratching) and use descriptive definitions (e.g. prolonged scratching of the back).'
    r = 'Enjoy! \n\n------------------------------------------------------------------------'

    prompt_list = [a,b,c,d,e,g,h,i,j,m,n,o,p,q]

    print()
    print(welcome)
    y = input(instr)
    

    while y != 'x':
        for x in prompt_list:
            print(x)
            z = input('')
            y = z
##            this makes the intro timed, but it's less engaging for the user:
##            
##            words = x.split(' ')
##            num_words = len(words)
##            wait = float(num_words)
##            time.sleep(wait)
        print(r)
        print()
        break

    t = Tool_System_Builder()
    s = t.make_3l_system()
    complete = 'Your tool system is complete. Find it here:' + s
    print(complete)
