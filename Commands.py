import sublime
import sublime_plugin
import os
from Default.exec import ExecCommand
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config
from Looplex_Lawtex_ST3_Plugin.lib.Validate_lawtex_file import Validate_lawtex_file
from Looplex_Lawtex_ST3_Plugin.lib.Upload_lawtex_template import Upload_lawtex_template

class LawtexSyntaxErrorHighlightListener(sublime_plugin.EventListener) :
    def on_load_async(self, view) :
        Config.check_plugin_jar_dependencies()

    def on_pre_save(self,view) :
        Config.check_plugin_jar_dependencies()

class Validate_lawtex_fileCommand(ExecCommand) :
    def run(self, **kwargs) :
        Config.check_plugin_jar_dependencies()
        vldService = Validate_lawtex_file(sublime.active_window().active_view())
        vldService.validate(sublime.message_dialog)

class Upload_lawtex_templateCommand(sublime_plugin.TextCommand) :
    def run(self,edit) :
        Config.check_plugin_jar_dependencies()
        uplService = Upload_lawtex_template(self.view)
        uplService.upload()

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
