import os
import subprocess
import time
import shutil #modul care permite sa stergi

#verifica daca sistemul de operar e Windows
if os.name == "nt":
    python_command ="python"
# In caz contrar Mac / Linux
else:
    python_command ="python3"


def create_project(project_name="test_project"):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    subprocess.call(CREATE_PROJECT_CMD, shell = True)

def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)

def create_application(app_name ="test_app", project_name="test_project"):
    #Current working directory
    cwd = os.getcwd()
    # imi schimba path-ul
    os.chdir(os.path.join(cwd, project_name))
    CREATE_APP_CMD = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell = True)

def _add_app_to_installed_apps(app_name ="test_app", project_name="test_project"):
     #Current working directory
    cwd = os.getcwd()
    # imi schimba path-ul
    os.chdir(os.path.join(cwd, project_name))

    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name))

    with open("settings.py", 'r') as freader:
        settings_content = freader.readlines()
        print(settings_content)

    has_encounter_installed_apps = False
    for index, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            has_encounter_installed_apps = True
        elif has_encounter_installed_apps and ("]" in line):
            settings_content.insert(index, f"\t'{app_name}', \n")
            break
    
    with open("settings.py", "w") as fwriter:
        fwriter.writelines(settings_content)



# Creează folderul templates
def create_templates_folder(app_name ="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, app_name))
    TEMPLATES = "templates"
    os.makedirs(TEMPLATES, exist_ok=True)

#Creeaza urls.py

def _create_urls_files(app_name ="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, app_name))
    URLS_FILE_NAME = "urls.py"
    URLS_CONTENT = """from django.urls import path\n\nurlpatterns = [\n\n]\n"""
    with open(URLS_FILE_NAME, "w") as fwriter:
        fwriter.write(URLS_CONTENT)

   

if __name__ == "__main__":
    #print(os.getcwd())

    # create_project()
    # time.sleep(3)
    # create_application()
    #delete_project()
    #_add_app_to_installed_apps()
    #create_templates_folder()

    _create_urls_files()








