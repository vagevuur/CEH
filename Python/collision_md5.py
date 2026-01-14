import hashlib

# Twee verschillende byte-sequenties met dezelfde MD5-hash
msg1 = bytes.fromhex(
  "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
  "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
  "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
  "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
)

msg2 = bytes.fromhex(
  "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89"
  "55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b"
  "d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0"
  "e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
)

md5_1 = hashlib.md5(msg1).hexdigest()
md5_2 = hashlib.md5(msg2).hexdigest()

print("MD5 hash msg1:", md5_1)
print("MD5 hash msg2:", md5_2)

print("\nBestanden gelijk?", msg1 == msg2)
print("Hashes gelijk?", md5_1 == md5_2)
