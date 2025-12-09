import hashlib

def sha256(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

files = [ "raw/ev_raw.csv", "raw/raw_air_quality.csv"]

for file in files:
    print(f"{file}: {sha256(file)}")