import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': True            
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT with WS281x LED',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 4-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'led_off_mode': 1,
    'led_off_color': 0xFFFF99,
    'led_wakeup_mode': 2,
    'led_wakeup_color': 0x33FFFF,    
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['volume'] = []
data['volume'].append({
    'value': 75,
    'type': 'event'    
})
data['hotword_engine'] = []
# data['hotword_engine'].append({
    # 'name': 'snowboy',
    # 'is_active': False
# })
data['hotword_engine'].append({
    'name': 'porcupine',
    'is_active': True,
    'porcupine_access_key': 'EhpBuTJggF/KvZ3fdsfsdfIsehkxbi4IwUtAONg=='
})
data['hotword'] = []
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-oh-vi_en_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-o-vi_en_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'alexa_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'bumblebee_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'computer_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grapefruit_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grasshopper_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey barista_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'jarvis_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'pico clock_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'picovoice_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'porcupine_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['continuous_asking'] = []
data['continuous_asking'].append({
    'content': 'hỏi liên tục',
    'is_active': True
})

data['internet_timeout'] = []
data['internet_timeout'].append({
    'internet_timeout': 5,    
})

data['check_url'] = []
data['check_url'].append({
    'check_url': 'http://www.google.com',
})

data['button_control'] = []
data['button_control'].append({
    'gpio_address': 11,
    'function': 'volume_up',
    'is_active': True    
})
data['button_control'].append({
    'gpio_address': 12,
    'function': 'volume_down',
    'is_active': True    
})
data['button_control'].append({
    'gpio_address': 13,
    'function': 'toggle_mic',
    'is_active': True    
})
data['button_control'].append({
    'gpio_address': 14,
    'function': 'direct_command',
    'is_active': True    
})


with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
