import re
from collections import defaultdict
import unittest

def extract_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    pattern = r'<(th|td)>(.*?)</\1>'
    tags = re.findall(pattern, html_content, re.DOTALL)
    return tuple(tags)

def clean_tags(tag_tuples):
    data_dict = defaultdict(list)
    for tag, content in tag_tuples:
        data_dict[tag].append(content.strip())
    return data_dict

class TestHTMLTagFunctions(unittest.TestCase):
    def test_extract_tags(self):
        tags = extract_tags('Dwarfplanets.html')
        print("Extracted Tags:", tags)
        self.assertTrue(len(tags) > 0)

    def test_clean_tags(self):
        tags = extract_tags('Dwarfplanets.html')
        cleaned = clean_tags(tags)
        print("Cleaned Tags Dictionary:", dict(cleaned))
        self.assertTrue(all(tag_type in cleaned for tag_type in ['th', 'td']))

if __name__ == '__main__':
    unittest.main()