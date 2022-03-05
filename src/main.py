from log import *
from application_log import *

def main():
    applog = ApplicationLog("MySecretApp.com.Transaction.Manager", 
                            "Starting transaction for session " + 
                            "-464410bf-37bf-475a-afc0-498e0199f008")
    applog.writeLog()
    return

if __name__ == "__main__":
    main()