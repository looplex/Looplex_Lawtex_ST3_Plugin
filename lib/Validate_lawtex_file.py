import sublime
import re
from looplex_lawtex_plugin.lib.Config import Config
from looplex_lawtex_plugin.lib.Select_ambient import Select_ambient
from looplex_lawtex_plugin.lib.Save_login_info import Save_login_info

class Validate_lawtex_file() :
    def __init__(self, view) :
        self.view = view
        self.view.erase_regions('LawtexSyntaxErrorHighlightListener')

    def validate(self, onPostSave) :
        if not Config.check_if_in_lawtex_file(self.view) :
            return

        self.onPostSave = onPostSave
        self.set_user()

    def set_user(self):

        self.looplexEnviron = Config.looplexEnvirons
        self.lawtexSettings = Config.load_lawtex_settings()

        for environ in reversed(self.looplexEnviron) :
            if not self.lawtexSettings.get(environ + "_username") == None :
                self.user = self.lawtexSettings.get(environ + "_username")
                self.validate_file()
                return

        self.retrieve_user()

    def retrieve_user(self):

        sublime.message_dialog("Salve um usuário antes de validar um arquivo!")

        setAmbService = Select_ambient(self.view)
        setAmbService.select_ambient(self.setup_user)

    def setup_user(self, ambient):
        self.ambient = ambient

        savLogService = Save_login_info(self.view)
        savLogService.save_and_callback(self.ambient, self.set_user)

    def validate_file(self):

        validate_context = "{\"currentFile\":\"" + self.view.file_name() + "\",\"username\":\"" + self.user + "\",\"command\":\"VALIDATE_FILE\"}"

        utilCall = Config()
        stdout = utilCall.run_jar_dependency_in_background(validate_context)

        if not stdout == None :
            self.verify_results(stdout)

    def verify_results(self, stdout) :
        print(stdout)
        validated = re.search("OKAY: The file has been validated!", stdout, re.DOTALL)
        if not validated:
            self.highlight_errors(stdout)
            if not self.onPostSave == None :
                error = re.search("(Issues at the file (?:[^\n]*\n){3})", stdout, re.DOTALL)
                self.onPostSave(error.group(1))
        else:
            if not self.onPostSave == None :
                self.onPostSave("OKAY: O programa foi aceito sintaticamente.")

    def highlight_errors(self, stdout) :
        m = re.search("(?:line\\s)(\\d+)", stdout, re.DOTALL)
        if m:
            row = m.group(1)
        else :
            sublime.message_dialog(stdout)
            return

        highlight_region = self.view.line( sublime.Region( self.view.text_point(int(row) - 1, 0), self.view.text_point(int(row) - 1, 0)))
        self.view.add_regions('LawtexSyntaxErrorHighlightListener', [highlight_region], "invalid", '', sublime.DRAW_SOLID_UNDERLINE)

        self.view.sel().clear()
        self.view.sel().add(highlight_region.end())
        self.view.show_at_center(highlight_region)