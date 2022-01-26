import sublime
import subprocess
import re
import os

class Config:

    pluginName = 'Looplex_Lawtex_ST3_Plugin'

    pluginJar = 'looplex_lawtex_plugin-1.5.jar'

    mainDataFolder = 'Looplex_Lawtex_ST3_Plugin'
    logsDataSubFolder = 'logs'
    databaseDataSubFolder = 'local_database'

    def check_if_in_lawtex_file(view):

        try :

            file_name = view.file_name()

            if file_name is not None:

                if re.search(r"\.lawtex$", view.file_name()):

                    if not view.is_dirty():
                        return True
                    else:
                        sublime.message_dialog("There are unsaved changes on your file, please save them or open it unchanged before validating it.")
                        return False

        except TypeError as error:
            pass

        sublime.error_message("Rode este comando em um arquivo .lawtex salvo!")
        return False

    @staticmethod
    def run_jar_dependency_in_background(context) :

        if sublime.platform() == "windows":
            CREATE_NO_WINDOW = 0x08000000
            context = context.replace("\\", "\\\\")
            win_jar_filepath = Config.retrieve_jar_dependency_filepath( "windows" )
            win_jre_filepath = Config.retrieve_jre_dependency_filepath( "windows" )
            subprocess.Popen([ win_jre_filepath, '-jar', win_jar_filepath, context ], creationflags = CREATE_NO_WINDOW )

        else :
            linux_jar_filepath = Config.retrieve_jar_dependency_filepath( "linux" )
            subprocess.Popen([ "java", "-jar", linux_jar_filepath, context ])

    @staticmethod
    def retrieve_jar_dependency_filepath( os_name ) :

        return os.path.join(sublime.packages_path(), Config.pluginName, 'jar', os_name, Config.pluginJar)

    @staticmethod
    def retrieve_jre_dependency_filepath( os_name ) :

        return os.path.join(sublime.packages_path(), Config.pluginName, 'jre', os_name, 'bin', 'java.exe')

    def retrieve_logs_folder_linux() :

        try :
            os.mkdir(os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.logsDataSubFolder))

        except OSError as error:
            pass

        return os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.logsDataSubFolder)

    def retrieve_database_folder_linux() :

        try :
            os.mkdir(os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.databaseDataSubFolder))

        except OSError as error:
            pass

        return os.path.join(os.getenv("HOME"), Config.mainDataFolder, Config.databaseDataSubFolder)

    def retrieve_logs_folder_windows() :

        folderPath = os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.logsDataSubFolder)

        if not os.path.exists( folderPath ):
            os.makedirs( folderPath )

        return os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.logsDataSubFolder)

    def retrieve_database_folder_windows() :

        folderPath = os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.databaseDataSubFolder)

        if not os.path.exists( folderPath ):
            os.makedirs( folderPath )

        return os.path.join(os.path.expanduser('~'), Config.mainDataFolder, Config.databaseDataSubFolder)