import re
pat = re.compile('[a-z]+')

m = pat.match('tem12po')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print()

mm = re.match(r'[a-z]+', 'tem12po')
print(mm)
print()

s = pat.search('3tem12po')
print(s)
if not s==None:
    print(s.group())
    print(s.start())
    print(s.end())
    print(s.span())

print()
f = pat.findall('tem12po')
print(f)