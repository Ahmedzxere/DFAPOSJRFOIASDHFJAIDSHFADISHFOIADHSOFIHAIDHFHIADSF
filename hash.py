import hashlib
from datetime import datetime, timedelta

validity_duration = timedelta(minutes=10)

creation_time = datetime.now()

def format_and_capitalize(text):
    first_20_chars = text[:20]
    capitalized_text = first_20_chars.upper()
    formatted_text = '-'.join([capitalized_text[i:i+5] for i in range(0, len(capitalized_text), 5)])
    return formatted_text

def generate_hashed_text():
    current_time = datetime.now()
    if current_time - creation_time > validity_duration:
        global creation_time
        creation_time = current_time
        text_to_hash = str(current_time.day)
    else:
        text_to_hash = str(current_time.day)
        
    hash_object = hashlib.sha256()
    hash_object.update(text_to_hash.encode('utf-8'))
    hashed_text = format_and_capitalize(hash_object.hexdigest())
    return hashed_text

print("admin kay  " + str(creation_time.day) + " > " + generate_hashed_text() + '\n')

for i in range(1, 6):
    hashed_text = generate_hashed_text()
    print("kay " + hashed_text + '\n')
