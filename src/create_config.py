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
data['volume'] = []
data['volume'].append({
    'value': 50,
    'type': 'speak'    
})
data['volume'].append({
    'value': 50,
    'type': 'event'    
})
data['hotword'] = []
data['hotword'].append({
    'name': 'hey siri',
    'keyword_path': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'americano',
    'keyword_path': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'blueberry',
    'keyword_path': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'terminator',
    'keyword_path': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'ok google',
    'keyword_path': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'hey google',
    'keyword_path': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True   
})

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)