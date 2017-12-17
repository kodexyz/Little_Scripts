from subprocess import run, PIPE

def r(command):
    """
    Run command and return output as a string
    :param command: Command to be executed
    :return: return string
    """
    return run(command, shell=True, stdout=PIPE, stderr=PIPE).stdout.decode()

#  who needs regular expressions when you got list comprehensions >:)
_output = [x for x in (r(command='xinput |grep Pen').split('\n'))]
pen = [x.strip("id=") for x in _output[0].split() if "id" in x][0]
pressure = [x.strip("id=") for x in _output[1].split() if "id" in x][0]

SCREEN = "DVI-I-1"

def reset(device_number):
    r(command="xinput disable " + device_number)
    r(command="xinput enable " + device_number)


def map_to_screen(device_number, display):
    r(command="xinput map-to-output " + device_number + ' ' + display)


def main(par=0):
    print(par)
    print("Resettinggggg")
    reset(pen)
    reset(pressure)
    map_to_screen(pen, SCREEN)


if __name__ == "__main__":
    main()

## Zucy loves this bunch of code
