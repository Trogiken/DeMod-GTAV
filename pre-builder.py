import os
from shutil import rmtree
cwd = os.getcwd()

# Verify Pyinstaller is installed
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
app = f'{cwd}\\app'
update = f'{cwd}\\update'
verify = True

app_required = ['main.py', 'mode_edit.py', 'class_animation.py', 'class_threadloading.py']
compare_app = []
app_missing = []
app_files = os.listdir(app)
for file in app_files:
    if file in app_required:
        compare_app.append(file)
if len(app_required) != len(compare_app):  # If all required files aren't found
    verify = False
    for f in app_required:
        if f not in compare_app:
            app_missing.append(f)
    print(f'Required files Missing from: {app}\n{app_missing}')

update_required = ['updater.py']
compare_update = []
update_missing = []
updater_files = os.listdir(update)
for file in updater_files:
    if file in update_required:
        compare_update.append(file)
if len(update_required) != len(compare_update):  # If all required files aren't found
    verify = False
    for f in update_required:
        if f not in compare_update:
            update_missing.append(f)
    print(f'Required files Missing from: {update}\n{update_missing}')

if verify is False:  # If any of the required files are missing
    input('\nPress ENTER to exit')
    exit()


# Create BUILD folders
build_dir = f'{cwd}\\BUILD'
app_dir = f'{build_dir}\\app'
update_dir = f'{build_dir}\\update'
misc_dir = f'{build_dir}\\__misc__'

if os.path.exists(build_dir):  # Clear BUILD folder
    try:
        rmtree(build_dir)
    except BaseException as rmerr:
        input(f'Failed to clear the BUILD folder\nERROR: {rmerr}')
        exit()
try:
    os.mkdir(build_dir)
    os.mkdir(app_dir)
    os.mkdir(update_dir)
    os.mkdir(misc_dir)
except BaseException as mkerr:
    input(f'Failed to create BUILD folders\nERROR: {mkerr}')
    exit()
