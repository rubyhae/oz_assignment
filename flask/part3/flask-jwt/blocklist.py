BLOCKLIST = set()

def add_to_blocklist(jtil):
    BLOCKLIST.add(jtil)

def remove_from_blocklist(jtil):
    BLOCKLIST.discard(jtil)