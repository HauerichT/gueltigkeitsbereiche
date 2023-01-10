wort = "test wort"


def scopes():
    wort = "scopes wort"

    def do_local():
        wort = "local wort"
        print("in do-local: " + wort)

    def do_nonlocal():
        nonlocal wort
        wort = "nonlocal wort"
        print("in do-nonlocal: " + wort)

    def do_global():
        global wort
        wort = "global wort"
        print("in do-global: " + wort)

    def print_scopes():
        print("in scopes: " + wort)

    for i in range(4):
        if i == 1:
            do_local()
        if i == 2:
            do_nonlocal()
        if i == 3:
            do_global()
        print("in scopes: " + wort)


for i in range(2):
    if i == 1:
        scopes()
    print("im Hauptprogramm: " + wort)


