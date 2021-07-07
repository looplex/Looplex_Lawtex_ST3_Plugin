import sublime
import subprocess
import re
import os
from zipfile import ZipFile

class Config:

    pluginName = 'looplex_lawtex_plugin'

    pluginJar = 'looplex_lawtex_plugin-1.1-SNAPSHOT.jar'

    lawtexSettingsFilename = 'looplex_lawtex_plugin.sublime-settings'

    mainDataFolder = 'Lawtex_ST3_Plugin'
    logsDataSubFolder = 'logs'
    databaseDataSubFolder = 'local_database'

    looplexEnvirons = ['SANDBOX', 'TESTING', 'STAGING']

    userInputPrompts = ['Insira seu usuário:', 'Insira sua senha:']
    userInputDefaults =  ['Username', 'Password']

    def load_lawtex_settings() :
        return sublime.load_settings(Config.lawtexSettingsFilename)

    def check_if_in_lawtex_file(view):
        if re.search(r"\.lawtex$", view.file_name()):
            if not view.is_dirty():
                return True
            else:
                sublime.message_dialog("There are unsaved changes on your file, please save them or open it unchanged before validating it.")
                return False
        else :
            sublime.error_message("Rode este comando em um arquivo .lawtex salvo!")
            return False

    def check_plugin_jar_dependencies():
        if not os.path.exists(Config.retrieve_jar_dependency_filename()):
            with ZipFile( os.path.dirname( os.path.dirname(__file__) ), 'r') as zip_obj:
                zip_obj.extract('jar/' + Config.pluginJar, os.path.join(sublime.packages_path(), Config.pluginName))

    def retrieve_jar_dependency_filename() :
        return os.path.join(sublime.packages_path(), Config.pluginName, 'jar', Config.pluginJar)

    def retrieve_logs_folder_linux() :
        try :
            os.mkdir(os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.logsDataSubFolder))
        except OSError:
            pass
        return os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.logsDataSubFolder)

    def retrieve_database_folder_linux() :
        try :
            os.mkdir(os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.databaseDataSubFolder))
        except OSError:
            pass
        return os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.databaseDataSubFolder)

    def retrieve_logs_folder_windows() :
        try :
            os.mkdir(os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.logsDataSubFolder))
        except OSError:
            pass
        return os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.logsDataSubFolder)

    def retrieve_database_folder_windows() :
        try :
            os.mkdir(os.path.join(os.path.expanduser('~'), 'Documents', Config.mainDataFolder, Config.databaseDataSubFolder))
        except OSError:
            pass
        return os.path.join(os.path.expanduser('~'), 'Documents', Config.mainDataFolder, Config.databaseDataSubFolder)

    def run_jar_dependency(self, context) :
        if sublime.platform() == "windows":
            context = context.replace("\\", "\\\\")
        jar_filepath = Config.retrieve_jar_dependency_filename()

        try:
            if sublime.platform() == "windows":
                CREATE_NO_WINDOW = 0x08000000
                process = subprocess.Popen(["java", "-jar", jar_filepath, context], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags = CREATE_NO_WINDOW)
            else :
                process = subprocess.Popen(["java", "-jar", jar_filepath, context], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, err = process.communicate()

            if not stdout == None:
                return stdout.decode("utf-8",'ignore')
            else:
                return stdout

        except subprocess.CalledProcessError as e:
            # TODO: Locale treatment
            sublime.error_message("An error occured while attempting to run the .jar dependency:\n\n" + str(e) + "\n\nPlease double-check your installation!")
            return None

    def run_jar_dependency_in_background(self, context) :
        if sublime.platform() == "windows":
            context = context.replace("\\", "\\\\")
        jar_filepath = Config.retrieve_jar_dependency_filename()

        if sublime.platform() == "windows":
            CREATE_NO_WINDOW = 0x08000000
            subprocess.Popen(["java", "-jar", jar_filepath, context], creationflags = CREATE_NO_WINDOW)
        else :
            subprocess.Popen(["java", "-jar", jar_filepath, context])