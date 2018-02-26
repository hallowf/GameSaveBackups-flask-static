import savebackup
import eel

@eel.expose
def call_backup():
    savebackup.make_backup()
eel.init("web")
eel.start("index.html")
