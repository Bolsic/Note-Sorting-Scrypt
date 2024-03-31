import markdown
import toml
import os

KEY_VALUE_PAIRS_PATH = '/home/basic/DnD/DnD-Notes/Waterdeep/unsorted/keys.toml' 
TARGET_DIRECTORY = '/home/basic/DnD/DnD-Notes/Waterdeep/unsorted'
OBSIDIAN_VAULT_PATH = '/home/basic/DnD/DnD-Notes/Waterdeep'
FILE_EXEPTIONS = ['keys.toml']

def read_markdown_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
        return markdown_text
    
# Tags are syntaxed as "#tag"
def get_tags(text):
    tags = []
    for line in text.split('\n'):
        for word in line.split(' '):
            if word.startswith('#'):
                word = word[1:]
                if not word.startswith('#'):
                    tags.append(word)
    return tags

def read_key_value_pairs(text):
    key_value_pairs = {}
    keys = toml.load(KEY_VALUE_PAIRS_PATH)
    return keys

def get_new_path(file_path, obsidian_vault_path=OBSIDIAN_VAULT_PATH):
    file_name = file_path.split('/')[-1]
    text_content = read_markdown_text(file_path)
    tags = get_tags(text_content)
    keys = read_key_value_pairs(KEY_VALUE_PAIRS_PATH)
 
    for tag in tags:
        if tag in keys:
            new_path = os.path.join(obsidian_vault_path, keys[tag], file_path.split('/')[-1])
        else:
            new_path = os.path.join(obsidian_vault_path, 'unsorted', file_path.split('/')[-1])

        print("Moved file:", file_name, "--->", new_path)
        return new_path

def sort_files(target_directory=TARGET_DIRECTORY, file_exceptions=FILE_EXEPTIONS, keys_path=KEY_VALUE_PAIRS_PATH, obsidian_vault_path=OBSIDIAN_VAULT_PATH):
    
    for filename in os.listdir(target_directory):
        if filename not in file_exceptions:
            file_path = os.path.join(target_directory, filename)

            new_path = get_new_path(file_path)
            
            os.rename(file_path, new_path)   

sort_files()





