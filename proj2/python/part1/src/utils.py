import numpy as np

def generateRandomMatrix(N, M):
    K = np.round(np.random.uniform(0, 255, size=(N, M)),3)
    return K

def printSignature():
    print("""\
                       .-.   _ .-.                          
                       : :  :_;: :                          
,-.,-.,-. .--.  .--.   : :  .-.: `-. .--.  .--.  .--. .-..-.
: ,. ,. :'  ..'`._-.'  : :_ : :' .; :: ..'' .; ; : ..': :; :
:_;:_;:_;`.__.'`.__.'  `.__;:_;`.__.':_;  `.__,_;:_;  `._. ;
                                                       .-. :
                                                       `._.'
        """)