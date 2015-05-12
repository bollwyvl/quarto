try:
    from jupyterpip import cmdclass
except:
    import pip, importlib
    pip.main(["install", "jupyter-pip"])
    cmdclass = importlib.import_module("jupyterpip").cmdclass
