import sublime
from Looplex_Lawtex_ST3_Plugin.lib.Config import Config

class Change_login_context() :

    def __init__(self, view) :
        
        self.view = view

    def changeContext(self) :

        change_context = "{\"command\":\"CHANGE_LOGIN_CONTEXT\",\"lang\":\"pt-BR\"}"

        Config.run_jar_dependency_in_background(change_context)
