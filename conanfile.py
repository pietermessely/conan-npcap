from conans import ConanFile, CMake, tools


class npcapConan(ConanFile):
    name = "npcap"
    version = "1.07"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Steganography here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "build_tests": [True, False]}
    default_options = "shared=False", "build_tests=False"
    generators = "cmake"
    #exports_sources = "src/*"

    def export_sources(self):
        self.output.info("Executing export_sources() method")
        self.copy('*', src="Include", dst="Include")
        self.copy('*', src="Lib", dst="lib")

    def build(self):
        cmake = CMake(self)
        #cmake.definitions["BUILD_TESTS"] = self.options.build_tests
        #cmake.configure()
        #cmake.build()
        #if self.options.build_tests:
        #    cmake.test()

    def package(self):
        self.copy("*.h", dst="Include", src="Include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ['Include']  # Ordered list of include paths

