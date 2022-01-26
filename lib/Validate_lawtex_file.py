import sublime
import re
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config

class Validate_lawtex_file() :

    def __init__(self, view) :

        self.view = view
        self.view.erase_regions('LawtexSyntaxErrorHighlightListener')

    def validate(self, onPostSave) :

        if not Config.check_if_in_lawtex_file(self.view) :
            return

        self.onPostSave = onPostSave
        self.validate_file()

    def validate_file(self):

        validate_context = "{\"currentFile\":\"" + self.view.file_name() + "\",\"lang\":\"pt-br\",\"command\":\"VALIDATE_LAWTEX_FILE\"}"

        Config.run_jar_dependency_in_background(validate_context)

    #     if not stdout == None :
    #         self.verify_results(stdout)

    # def verify_results(self, stdout) :

    #     print(stdout)

    #     validated = re.search("OKAY: The file has been validated!", stdout, re.DOTALL)

    #     if not validated:

    #         self.highlight_errors(stdout)

    #         if not self.onPostSave == None :

    #             error = re.search("(Issues at the file (?:[^\n]*\n){3})", stdout, re.DOTALL)
    #             self.onPostSave(error.group(1))

    #     else:

    #         if not self.onPostSave == None :

    #             self.onPostSave("OKAY: O programa foi aceito sintaticamente.")

    # def highlight_errors(self, stdout) :

    #     m = re.search("(?:line\\s)(\\d+)", stdout, re.DOTALL)

    #     if m:
    #         row = m.group(1)
    #     else :
    #         sublime.message_dialog(stdout)
    #         return

    #     highlight_region = self.view.line( sublime.Region( self.view.text_point(int(row) - 1, 0), self.view.text_point(int(row) - 1, 0)))
    #     self.view.add_regions('LawtexSyntaxErrorHighlightListener', [highlight_region], "invalid", '', sublime.DRAW_SOLID_UNDERLINE)

    #     self.view.sel().clear()
    #     self.view.sel().add(highlight_region.end())
    #     self.view.show_at_center(highlight_region)