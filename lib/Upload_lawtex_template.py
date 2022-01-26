import sublime
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config

class Upload_lawtex_template():

    def __init__(self, view):

        self.view = view

    def upload(self) :

        if not Config.check_if_in_lawtex_file(self.view) :
            return

        self.execute_upload_dependency()

    def execute_upload_dependency(self) :
        
        login_context = "{\"initialFile\":\"" + sublime.active_window().active_view().file_name() + "\",\"command\":\"UPLOAD_LAWTEX_TEMPLATE\",\"lang\":\"pt-br\"}"

        Config.run_jar_dependency_in_background(login_context)