from cx_Freeze import setup, Executable
setup(
    name = "Campo Minado",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["funcoes"],
        'include_files': ['imagens'],
        'include_msvcr': True,
    }},
    executables = [        Executable(
            "app.py",
            copyright="Copyright (C) 2022 cx_Freeze",
            base="Win32GUI",
            icon="imagens/CM.ico",
            shortcutName="Campo Minado",
            shortcutDir="DesktopFolder"
            )]
    )