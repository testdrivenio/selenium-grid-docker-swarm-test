from subprocess import Popen


processes = []

for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome && python project/test.py'
    firefox_cmd = 'export BROWSER=firefox && python project/test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(10):
    processes[counter].wait()
