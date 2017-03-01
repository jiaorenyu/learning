import sys

from pybloomd import BloomdClient

def parse_line(line):
    line = line.strip()

    key_tids = line.split()

    device_id = key_tids[0]
    tid_list = key_tids[1].split(",")

    return device_id, tid_list

if __name__ == "__main__":
    fn = sys.argv[1]
    tid = sys.argv[2]

    
    # Create a client to a local bloomd server, default port
    client = BloomdClient(["localhost:8673"])

    with open(fn) as fp:
        for line in fp:
            device_id, tid_list = parse_line(line)
            
            if tid in tid_list:
                client[tid+"_a"].add(device_id)

    
    # Get or create the foobar filter
    #male = client.create_filter("10000_a")
