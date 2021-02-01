from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools


class AppConan(ConanFile):
    name = "app"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*"
    requires = "poco/1.9.4"

    def build(self):
        print("Building...")
        with tools.chdir("src"):
            atools = AutoToolsBuildEnvironment(self)
            atools.make()

    def package(self):
        print("Packaging...")
        self.copy("*app", dst="bin", keep_path=False)
        self.copy("*app.exe", dst="bin", keep_path=False)

    def deploy(self):
        print("Deploying...")
        self.copy("*", src="bin", dst="bin")