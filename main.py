wort = "test wort"


def scopes():
    wort = "scopes wort"

    def do_local():
        wort = "local wort"
        print("in do-local: " + wort)
        print_scopes()

    def do_nonlocal():
        nonlocal wort
        wort = "nonlocal wort"
        print("in do-nonlocal: " + wort)
        print_scopes()

    def do_global():
        global wort
        wort = "global wort"
        print("in do-global: " + wort)
        print_scopes()

    def print_scopes():
        print("in scopes: " + wort)

    print_scopes()
    do_local()
    do_nonlocal()
    do_global()


for i in range(3):
    if i == 0 or i == 2:
        print("im Hauptprogramm: " + wort)
    if i == 1:
        scopes()


