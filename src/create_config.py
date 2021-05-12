import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 2/4-Mics Pi HAT',
    'is_active': True        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'is_active': False        
})    

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
