from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class LibjsonConan(ConanFile):
    name = "libjson"
    version = "7.6.1"
    license = "Copyright 2010 Jonathan Wallace. All rights reserved."
    url = "https://latesco.kixeye.com/projects/"
    description = "libjson is a high speed complete JSON library, including parsers, writers, builders, formatters, validators"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    unzipped_name = "libjson_%s" % version
    zip_name = "%s.zip" % unzipped_name

    def source(self):
        url = "http://sourceforge.net/projects/libjson/files/%s/download" % (self.zip_name)
        self.output.info("Downloading %s..." % url)

        tools.download(url, self.zip_name)
        tools.unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        with tools.chdir("./libjson"):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.flags = []  # libjson's makefile chokes if we pass this
            env_build.cxxflags = [] 
            self.run("make")  # Run make manually so AutoToolsBuildEnvironment doesn't pass the -j parameter. That breaks the build

    def package(self):
        self.copy("*.h", dst="include", src="libjson")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        # Copying debug symbols
        if self.settings.compiler == "Visual Studio" and self.options.include_pdbs:
            self.copy(pattern="*.pdb", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["json"]
