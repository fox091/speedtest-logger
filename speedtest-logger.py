import speedtest
import time
import sys
import csv

filename = time.strftime("%Y-%m-%d-%H-%M-%S")

filename += "-speedtest-results.csv"

print("Opening file " + filename)
with open(filename, "x") as f:
    csv_file_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = ["Timestamp (eastern)", "Download (mbps)", "Upload (mbps)"]
    csv_file_writer.writerow(headers)
    print("Wrote csv headers.")

    s = speedtest.Speedtest()
    s.get_closest_servers()

    print("Starting speedtest loop.")
    while True:
        try:
            timestamp = time.strftime("%Y-%m-%d-%I:%M:%S%p")
            s.download()
            s.upload()
            download = s.results.download / 1000000
            upload = s.results.upload / 1000000
            row = [timestamp, f"{download:.4f}", f"{upload:.4f}"]
            csv_file_writer.writerow(row)
            print("Finished a test.  Running again.")
        except KeyboardInterrupt:
            print("Quitting gracefully.")
            f.close()
            sys.exit(0)
