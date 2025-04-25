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


def create_project(project_name="test_project", *applications):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    subprocess.call(CREATE_PROJECT_CMD, shell = True)

    for app_name in applications:
        create_application(app_name, project_name)
        

def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)

def create_application(app_name ="test_app", project_name="test_project"):
    #Current working directory
    cwd = os.getcwd()
    # imi schimba path-ul
    os.chdir(os.path.join(cwd, project_name))

    CREATE_APP_CMD = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell = True)
    time.sleep(0.5)
    setup_application(app_name, project_name)

def setup_application(app_name ="test_app", project_name="test_project"):
    _add_app_to_installed_apps(app_name, project_name)
    create_templates_folder(app_name, project_name)
    _create_app_url_file(app_name, project_name)
    _link_app_in_project_url_file(app_name, project_name)

    

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

def _create_app_url_file(app_name ="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, app_name))
    URLS_FILE_NAME = "urls.py"
    URLS_CONTENT = """from django.urls import path\n\nurlpatterns = [\n\n]\n"""
    with open(URLS_FILE_NAME, "w") as fwriter:
        fwriter.write(URLS_CONTENT)

def _link_app_in_project_url_file(app_name ="test_app", project_name="test_project"):
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name, project_name))
    with open("urls.py", "r") as freader:
        urls_lines = freader. readlines()
    has_encounter_urlpatterns = False
    new_line = f"\tpath ('{app_name}/', include('{app_name}.urls')),\n"

    if new_line in urls_lines:
        return
    
    for index, line in enumerate(urls_lines):
        if 'from django.urls import path' in line and 'include' not in line:
            urls_lines[index] = line = line.replace("path", "path, include")
        if "urlpatterns = [" in line:
            has_encounter_urlpatterns = True
        elif has_encounter_urlpatterns and "]" in line:
            urls_lines.insert(index, new_line)
            break
    with open("urls.py", "w") as fwriter:
        fwriter.writelines(urls_lines)


if __name__ == "__main__":
    #print(os.getcwd())

    # create_project()
    # time.sleep(3)
    # create_application()
    #delete_project()
    #_add_app_to_installed_apps()
    #create_templates_folder()

    #_create_app_url_file()
    _link_app_in_project_url_file()







