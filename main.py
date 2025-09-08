import hashlib
s='miniplus'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
