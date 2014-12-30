import sublime, os, json

class NewModule:

    # package settings
    settings = None

    # path to where to insert directory
    basePath = ""

    # mappers list
    mappers = []

    def createModule(self):
        mappers = self.getMappers()
        self.window.show_quick_panel(mappers, self.setMapper)


    def getMappers(self):

        if not self.mappers:
            self.mappers = list(self.settings['mappers'].copy().keys()) if 'mappers' in self.settings else False

        if not self.mappers:
            sublime.error_message('No Mappers Found')

        return self.mappers

    def setMapper(self, moduleIndex):
        if moduleIndex >= 0:
            self.mapper = self.mappers[moduleIndex]
            self.getModuleName();
        else:
            pass

    def getModuleName(self):
        self.window.show_input_panel('Module Name', '', self.setModuleName, None, None)

    def setModuleName(self, name):
        self.name = name
        self.createStructure()

    def createStructure(self):
        structure = self.settings['mappers'][self.mapper]

        # create directories
        if 'directories' in structure.keys():
            self.createDirectories(structure['directories'])

        # create files
        if 'files' in structure.keys():
            self.createFiles(structure['files'])

    def createDirectories(self, directories):
        for directory in directories:
            directory = directory.replace('[[[ModuleName]]]', self.name)
            os.mkdir(self.basePath + directory)

    def createFiles(self, files):
        for newFile in files:
            newFile = newFile.replace('[[[ModuleName]]]', self.name)
            f = open(self.basePath + newFile, 'w+')
            f.close()