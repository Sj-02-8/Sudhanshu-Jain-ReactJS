import hashlib

def generate_script_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Example usage:
file_path = 'code3.py'
hash_value = generate_script_hash(file_path)
print(f"SHA256 Hash of {file_path}: {hash_value}")

