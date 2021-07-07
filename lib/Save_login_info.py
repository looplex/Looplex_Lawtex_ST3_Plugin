import sublime
import os
from looplex_lawtex_plugin.lib.Config import Config

class Save_login_info():
    def __init__(self, view):
        self.onDoneFunction = None
        self.view = view
        self.lawtexSettings = Config.load_lawtex_settings()

    def save_and_callback(self, ambient, onDoneFunction) :
        self.onDoneFunction = onDoneFunction
        self.save(ambient)

    def save(self, ambient) :
        self.ambient = ambient
        self.window = self.view.window()
        self.loginInfoCounter = 0
        self.retrieve_login_info()

    def retrieve_login_info(self) :
        panel = self.window.show_input_panel(Config.userInputPrompts[self.loginInfoCounter], Config.userInputDefaults[self.loginInfoCounter], self.on_done_retrieving_login_info, None, None)
        if Config.userInputDefaults[self.loginInfoCounter] == "Password" :
            panel.settings().set("password", True)
        else :
            panel.settings().set("password", False)

    def on_done_retrieving_login_info(self, inputText) :
        if self.loginInfoCounter == 0 :
            fieldName = "_username"
        elif self.loginInfoCounter == 1 :
            fieldName = "_password"

        self.lawtexSettings.set(self.ambient + fieldName, inputText)
        sublime.save_settings(Config.lawtexSettingsFilename)

        self.loginInfoCounter += 1

        if self.loginInfoCounter < len(Config.userInputPrompts) :
            self.retrieve_login_info()
        else:
            # TODO Localized text
            sublime.message_dialog("Usuário e senha salvos em " + os.path.join(sublime.packages_path(), 'User', Config.lawtexSettingsFilename) + " com sucesso!")
            if self.onDoneFunction is not None :
                self.onDoneFunction()