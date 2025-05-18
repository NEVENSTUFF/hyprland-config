import os
from packages import install
def main():
    install()
    print('packages installed')
    sleep(3)
    os.system('hyprland')
main()

