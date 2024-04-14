import re
from collections import defaultdict
import unittest

def extract_tags(html_content):
    pattern = r"(<(table|tr|th|td)\b[^>]*>.*?</\2>)"
    tags = re.findall(pattern, html_content, re.DOTALL)
    if not tags:
        print("No tags captured: Check regex and HTML content.")
    return tuple(tags)

def clean_tags(tags_tuple):
    tags_dict = defaultdict(list)
    for tag in tags_tuple:
        match = re.match(r"<(\w+)", tag)
        if not match:
            print(f"Tag did not match expected format: {tag}")
            continue
        tag_type = match.group(1)
        tags_dict[tag_type].append(tag.strip())
    return tags_dict

class TestHTMLTagFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_content = '''
        <table class="dwarfs">
            <tr>
                <th>Dwarf</th>
                <th>Distance(AU)</th>
                <th>Period</th>
            </tr>
            <tr>
                <td>Pluto</td>
                <td>39.5</td>
                <td>247.69</td>
            </tr>
            <tr>
                <td>Eris</td>
                <td>67.84</td>
                <td>558.77</td>
            </tr>
            <tr>
                <td>Haumea</td>
                <td>43.19</td>
                <td>283.84</td>
            </tr>
            <tr>
                <td>Makemake</td>
                <td>45.48</td>
                <td>306.17</td>
            </tr>
            <tr>
                <td>Ceres</td>
                <td>2.77</td>
                <td>4.61</td>
            </tr>
        </table>
        '''
    
    def test_extract_tags(self):
        extracted_tags = extract_tags(self.html_content)
        self.assertTrue(isinstance(extracted_tags, tuple), "Extracted tags should be a tuple")
        self.assertTrue(any('<table' in tag for tag in extracted_tags), "Table tags should be present in the extracted output")
        print("Extracted tags:", extracted_tags)  # Debugging output

    def test_clean_tags(self):
        extracted_tags = extract_tags(self.html_content)
        cleaned_tags = clean_tags(extracted_tags)
        self.assertTrue(isinstance(cleaned_tags, defaultdict))
        self.assertEqual(len(cleaned_tags['th']), 3)
        self.assertEqual(len(cleaned_tags['td']), 5)

if __name__ == '__main__':
    unittest.main()