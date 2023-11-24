
import subprocess

import string



def execute_command(command, text, punctuation_mode=False):

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output, error = process.communicate()



    if process.returncode == 0:

        if punctuation_mode:

            words = output.decode().split()

            words = [word.strip(string.punctuation) for word in words]

            return text in words

        else:

            return text in output.decode()



    return False
