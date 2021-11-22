import sublime
import subprocess
import re
import os
from zipfile import ZipFile

class Config:

    pluginName = 'Looplex_Lawtex_ST3_Plugin'

    pluginJar = 'looplex_lawtex_plugin-1.4.4.jar'

    mainDataFolder = 'Looplex_Lawtex_ST3_Plugin'
    logsDataSubFolder = 'logs'
    databaseDataSubFolder = 'local_database'

    def check_plugin_java_dependencies():

        if not os.path.exists( Config.retrieve_java_dependency_filepath() ):

            if sublime.platform() == "windows":

                with ZipFile( os.path.dirname( os.path.dirname(__file__) ), 'r') as zip_obj:

                    zip_obj.extract('java/windows', os.path.join(sublime.packages_path(), Config.pluginName))

            elif sublime.platform() == "osx":

                with ZipFile( os.path.dirname( os.path.dirname(__file__) ), 'r') as zip_obj:

                    zip_obj.extract('java/osx' + Config.pluginJar, os.path.join(sublime.packages_path(), Config.pluginName))

            else:

                with ZipFile( os.path.dirname( os.path.dirname(__file__) ), 'r') as zip_obj:

                    zip_obj.extract('java/linux' + Config.pluginJar, os.path.join(sublime.packages_path(), Config.pluginName))

    def retrieve_java_dependency_filepath() :

        return os.path.join(sublime.packages_path(), Config.pluginName, 'java')


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

        Config.check_plugin_java_dependencies()
        Config.check_plugin_jar_dependencies()

        if sublime.platform() == "windows":
            context = context.replace("\\", "\\\\")

        jar_filepath = Config.retrieve_jar_dependency_filepath()

        if sublime.platform() == "windows":
            CREATE_NO_WINDOW = 0x08000000
            subprocess.Popen([ os.path.join(sublime.packages_path(), Config.pluginName, "windows", "bin", "java"), "-jar", jar_filepath, context], creationflags = CREATE_NO_WINDOW)

        elif sublime.platform() == "osx":
            subprocess.Popen([ os.path.join(sublime.packages_path(), Config.pluginName, "osx", "Home", "bin", "java"), "-jar", jar_filepath, context])

        else :
            subprocess.Popen([ os.path.join(sublime.packages_path(), Config.pluginName, "linux", "bin", "java"), "-jar", jar_filepath, context])

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