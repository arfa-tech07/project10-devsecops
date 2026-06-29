import subprocess
user_input = input("enter command: ")
subprocess.run(["echo", user_input], check=True)