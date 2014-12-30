import sublime, sublime_plugin, os, json

class Q4NewModuleCommand(sublime_plugin.WindowCommand):

    def is_enabled(self, dirs, moduleType):
        return True if dirs else False

    def run(self, dirs, moduleType):
        self.packagePath = sublime.packages_path() + "/Quadrant4/"
        self.mapperPath  = self.packagePath + "mappers/"
        self.moduleType = moduleType;
        self.basePath = dirs[0] + "/";
        self.window.show_input_panel('Module Name', '', self.newModule, None, None)


    def newModule(self, name):
        # find mappers json file
        mapper = self.getMapper(self.moduleType)

        # get parsed module structure
        structure = self.getStructure(mapper, name)

        # create structure
        self.createStructure(structure)


    def getMapper(self, moduleType):
        mapper = self.mapperPath + moduleType + ".json"

        if (os.path.isfile(mapper)):
            return mapper
        else:
            sublime.error_message('Could not create module. Could not found file:'+"\n\n" + mapper + "\n\n"+'For type: ['+moduleType+']')


    def getStructure(self, mapper, name):
        contents = open(mapper).read()
        contents = contents.replace('[[[ModuleName]]]', name)

        return json.loads(contents)


    def createStructure(self, structure):
        # create directories
        if 'directories' in structure.keys():
            self.createDirectories(structure['directories'])

        # create files
        if 'files' in structure.keys():
            self.createFiles(structure['files'])


    def createDirectories(self, directories):
        for directory in directories:
            os.mkdir(self.basePath + directory)


    def createFiles(self, files):
        for newFile in files:
            f = open(self.basePath + newFile, 'w+')
            f.close()
