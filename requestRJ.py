import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(f'Status Code: {res.status_code}')
print(f'Length: {len(res.text)}')
print(f'Headers: {res.headers["content-type"]}')
print(f'Encoding: {res.encoding}')

print(f'First 500 chars: {res.text[:500]}')

playfile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playfile.write(chunk)


