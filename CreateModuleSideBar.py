import sublime, sublime_plugin, Quadrant4.new_module

class CreateModuleSideBarCommand(sublime_plugin.WindowCommand, Quadrant4.new_module.NewModule):

    # only enable option if a directory is selected
    def is_enabled(self, dirs):
        return True if dirs else False

    # only enable option if a directory is selected
    def is_visible(self, dirs):
        return True if dirs else False

    # run the module
    def run(self, dirs):
        self.basePath = dirs[0] + "/";
        self.settings = sublime.load_settings("Quadrant4.sublime-settings").get('new_module')
        self.createModule()