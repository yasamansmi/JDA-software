
author = "Yasaman Samiee"
email = "yasaman.msamiee@gmail.com"


from setuptools.command.build_py import build_py



class CustomBuildPyCommand(build_py):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):

        print(f"Yasaman: {self.packages}, {self.py_modules}")
        super().run()



def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    print("Called build")
    setup_kwargs.update({"cmdclass": {"build_py": CustomBuildPyCommand}})