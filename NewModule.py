import sublime, sublime_plugin

class Q4NewModuleCommand(sublime_plugin.WindowCommand):

    def run(self, dirs, type):
        self.type = type;
        self.window.show_input_panel('Module Name', '', self.newModule, None, None)

    def newModule(self, name):
        print(name, self.type)

    def is_enabled(self, dirs, type):
        return True if dirs else False