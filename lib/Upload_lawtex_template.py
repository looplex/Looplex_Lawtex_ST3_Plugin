import sublime
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config
from Looplex_Lawtex_ST3_Plugin.lib.Select_ambient import Select_ambient
from Looplex_Lawtex_ST3_Plugin.lib.Save_login_info import Save_login_info

class Upload_lawtex_template():
    def __init__(self, view, ambient):
        self.view = view
        self.ambient = ambient

    def upload(self) :
        if not Config.check_if_in_lawtex_file(self.view) :
            return

        if self.ambient == None :
            self.setAmbService = Select_ambient(self.view)
            self.setAmbService.select_ambient(self.setup_input)
        else :
            self.setup_input(self.ambient)

    def setup_input(self, ambient):
        self.ambient = ambient
        self.lawtexSettings = Config.load_lawtex_settings()

        if self.lawtexSettings.get(ambient + "_username") == None :
            savLogService = Save_login_info(self.view)
            savLogService.save_and_callback(self.ambient, self.set_input)
        else:
            self.set_input()

    def set_input(self) :
        self.username = self.lawtexSettings.get(self.ambient + "_username")
        self.password = self.lawtexSettings.get(self.ambient + "_password")

        self.execute_upload_dependency()

    def execute_upload_dependency(self) :

        if self.ambient == 'PRODUCTION' :
            login_context = "{\"currentFile\":\"" + sublime.active_window().active_view().file_name() + "\",\"command\":\"UPLOAD_TEMPLATE_TO_PRODUCTION\"}"
        else:
            login_context = "{\"currentFile\":\"" + sublime.active_window().active_view().file_name() + "\",\"username\":\"" + self.username +  "\",\"password\":\"" + self.password + "\",\"command\":\"UPLOAD_TEMPLATE\",\"ambient\":" + self.ambient + "}"

        utilCall = Config()
        utilCall.run_jar_dependency_in_background(login_context)