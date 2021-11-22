import sublime
import sublime_plugin
import os
from Default.exec import ExecCommand
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config
from Looplex_Lawtex_ST3_Plugin.lib.Validate_lawtex_file import Validate_lawtex_file
from Looplex_Lawtex_ST3_Plugin.lib.Upload_lawtex_template import Upload_lawtex_template
from Looplex_Lawtex_ST3_Plugin.lib.Change_login_context import Change_login_context

class Validate_lawtex_fileCommand(ExecCommand) :

    def run(self, **kwargs) :

        vldService = Validate_lawtex_file(sublime.active_window().active_view())
        vldService.validate(sublime.message_dialog)

class Upload_lawtex_templateCommand(sublime_plugin.TextCommand) :

    def run(self,edit) :

        uplService = Upload_lawtex_template(self.view)
        uplService.upload()

class Change_login_contextCommand(sublime_plugin.TextCommand) :

    def run(self,edit) :

        chngLoginService = Change_login_context(self.view)
        chngLoginService.changeContext()

class Open_logs_folderCommand(sublime_plugin.TextCommand) :

    def run(self,edit) :

        if sublime.platform() == "windows":

            os.startfile(Config.retrieve_logs_folder_windows())

        else :

            # Both Linus and OSX
            os.system('xdg-open "%s"' % Config.retrieve_logs_folder_linux())

class Open_database_folderCommand(sublime_plugin.TextCommand) :

    def run(self,edit) :

        if sublime.platform() == "windows":

            os.startfile(Config.retrieve_database_folder_windows())

        else :
            
            # Both Linus and OSX
            os.system('xdg-open "%s"' % Config.retrieve_database_folder_linux())
