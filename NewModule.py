import sublime, sublime_plugin, os, json

class Q4NewModuleCommand(sublime_plugin.WindowCommand):

    def is_enabled(self, dirs, type):
        return True if dirs else False

    def run(self, dirs, type):
        self.packagePath = sublime.packages_path() + "/Quadrant4/"
        self.mapperPath  = self.packagePath + "mappers/"
        self.type = type;
        self.basePath = dirs[0] + "/";
        self.window.show_input_panel('Module Name', '', self.newModule, None, None)

    def newModule(self, name):
        # find mappers json file
        self.findMapper(name)

        # create directories

        # create files

    def findMapper(self, name):
        # does file exist?
        mapperFile = self.mapperPath + self.type + ".json"
        if (os.path.isfile(mapperFile)):
            # read contents and replace tokens
            contents = open(mapperFile).read()
            contents = contents.replace('[[[ModuleName]]]', name)

            # convert to json
            structure = json.loads(contents)
            print(contents)
            print(structure)

            if 'directories' in structure.keys():
                self.createDirectories(structure['directories'])

            if 'files' in structure.keys():
                self.createFiles(structure['files'])

    def createDirectories(self, directories):
        for directory in directories:
            os.mkdir(self.basePath + directory)

    def createFiles(self, files):
        for newFile in files:
            f = open(self.basePath + newFile, 'w+')
            f.close()
