data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for d in data: #dict
    for k in key_list: #str
        if d.get(k) == None:
            d.setdefault(k, 'unKnown')
        print(f'{k}은/는 {d.get(k)}입니다.')
        #1 # value = d.get(k, 'unknown')
        #2 # d.setdefault(k, 'unknown')
        #1,2 # print(f'{k}은/는 {value}입니다.')
    print()

