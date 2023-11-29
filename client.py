import sys
import urllib.request

from pyarrow import ipc

if __name__ == "__main__":
    endpoint = sys.argv[1]
    method = sys.argv[2]

    with urllib.request.urlopen(f"{endpoint}/{method}") as response:
        with ipc.open_stream(response) as stream:
            for i, batch in enumerate(stream):
                print(f"Response batch {i}:")
                print(batch)
