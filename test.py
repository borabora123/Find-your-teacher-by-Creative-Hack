from requests import get, post, delete

print(get('http://elros.info/hackaton/form/').json())
print(get('http://localhost:5000/api/v2/lesson/4').json())
print(get('http://localhost:5000/api/v2/lesson/6').json())
print(get('http://localhost:5000/api/v2/lesson/q').json())
print(post('http://localhost:5000/api/v2/lesson').json())
print(post('http://localhost:5000/api/v2/lesson', json={'id': 3}).json())
print(post('http://localhost:5000/api/v2/lesson', json={
    'id': 2,
    'name': 'egor',
    'about': 'gfgndndndn',
    'email': 'vgv@fd/rru',
    'hashed_password': '3143ghshsg3252',
}).json())
print(delete('http://localhost:5000/api/v2/lesson/999').json())
print(delete('http://localhost:5000/api/v2/lesson/10').json())
