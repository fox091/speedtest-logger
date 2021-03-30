import speedtest
import time
from time import sleep
import sys

filename = time.strftime("%Y%m%d-%H%M%S")

filename += "-speedtest-results.csv"

print("Opening file " + filename)
with open(filename, "x") as f:
    # The OTT Communications server.
    servers = [1421]
    s = speedtest.Speedtest()

    wrote_headers = False

    print("Starting speedtest loop.")
    while True:
        try:
            s.get_servers(servers)
            s.download()
            s.upload()
            if wrote_headers == False:
                f.write(s.results.csv_header() + "\n")
                wrote_headers = True
            f.write(s.results.csv() + "\n")
            print("Finished a test.  Running again.")
        except KeyboardInterrupt:
            print("Quitting gracefully.")
            f.close()
            sys.exit(0)
