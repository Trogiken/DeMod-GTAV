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

# Verify File Locations
cwd = os.getcwd()
app = f'{cwd}\\app'
updater = f'{cwd}\\updater'
verify = True

app_required = ['main', 'mode_edit', 'class_animation', 'class_threadloading']
compare_app = []
app_files = os.listdir(app)
for file in app_files:
    if file in app_required:
        compare_app.append(file)
if app_required != compare_app:  # If all required files aren't found
    verify = False
    for file in app_required:
        if file in compare_app:
            app_required.remove(file)  # Leave remaining files that haven't been found
    print(f'Required files Missing from: {app}\nMissing Files [{app_required}]')

updater_required = ['updater']
compare_updater = []
updater_files = os.listdir(updater)
for file in updater_files:
    if file in updater_required:
        compare_updater.append(file)
if updater_required != compare_updater:  # If all required files aren't found
    verify = False
    for file in updater_required:
        if file in compare_updater:
            updater_required.remove(file)  # Leave remaining files that haven't been found
    print(f'Required files Missing from: {updater}\nMissing Files [{updater_required}]')

if verify is False:  # If any of the required files are missing
    input('Press ENTER to exit')
    exit()
