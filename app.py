import subprocess
user_input = input("enter command: ")
subprocess.call(user_input, shell=True)