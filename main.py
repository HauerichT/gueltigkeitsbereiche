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

    print("in scopes: " + wort)
    do_local()
    print("in scopes: " + wort)
    do_nonlocal()
    print("in scopes: " + wort)
    do_global()
    print("in scopes: " + wort)


print("im Hauptprogramm: " + wort)
scopes()
print("im Hauptprogramm: " + wort)
