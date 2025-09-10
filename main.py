import hashlib
s='kitalpha'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
