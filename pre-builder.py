import os

while True:
    installed = (os.system(f"pyinstaller"))
    os.system('cls')
    if installed == 1 or 2:  # 1 = not installed, 2 = installed
        if installed != 2:
            user = input("PyInstaller is not Installed on this System\nDo You Want to Install PyInstaller? (y, n)\n> ")\
                .casefold()
            if user == 'y':
                os.system("pip install pyinstaller")
                continue
            elif user == 'n':
                os.system('cls')
                exit()
            else:
                continue
        else:  # If pyinstaller is installed
            break
    else:
        input("Failed to Verify PyInstaller Status\nPress ENTER to exit")
        exit()
