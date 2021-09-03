import sublime
import subprocess
import re
import os
from zipfile import ZipFile

class Config:

    pluginName = 'Looplex_Lawtex_ST3_Plugin'

    pluginJar = 'Looplex_Lawtex_ST3_Plugin-1.3.jar'

    mainDataFolder = 'Looplex_Lawtex_ST3_Plugin'
    logsDataSubFolder = 'logs'
    databaseDataSubFolder = 'local_database'

    def check_plugin_jar_dependencies():
        if not os.path.exists( Config.retrieve_jar_dependency_filepath() ):
            with ZipFile( os.path.dirname( os.path.dirname(__file__) ), 'r') as zip_obj:
                zip_obj.extract('jar/' + Config.pluginJar, os.path.join(sublime.packages_path(), Config.pluginName))

    def retrieve_jar_dependency_filepath() :
        return os.path.join(sublime.packages_path(), Config.pluginName, 'jar', Config.pluginJar)

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

    def run_jar_dependency_in_background(self, context) :
        if sublime.platform() == "windows":
            context = context.replace("\\", "\\\\")
        jar_filepath = Config.retrieve_jar_dependency_filepath()

        if sublime.platform() == "windows":
            CREATE_NO_WINDOW = 0x08000000
            subprocess.Popen(["java", "-jar", jar_filepath, context], creationflags = CREATE_NO_WINDOW)
        else :
            subprocess.Popen(["java", "-jar", jar_filepath, context])

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