from Looplex_Lawtex_ST3_Plugin.lib.Config import Config

class Select_ambient():
    def __init__(self, view):
        self.view = view

    def select_ambient(self, onDoneFunction) :
        self.window = self.view.window()
        self.window.show_quick_panel(Config.looplexEnvirons, lambda id: self.on_done(id, onDoneFunction))

    def on_done(self, selectedAmbient, onDoneFunction) :
        if selectedAmbient >= 0 :
            onDoneFunction(Config.looplexEnvirons[selectedAmbient])