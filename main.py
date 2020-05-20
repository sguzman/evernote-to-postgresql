from typing import Optional
from typing import List
from typing import Tuple
import xml.etree.ElementTree as ET

path: str = './notes.enex'


def read_xml() -> List[str]:
    tree: ET = ET.parse(path)
    root: ET.ElementTree = tree.getroot()


    for child in root.getiterator():
        if child.tag == 'title':
            t: str = child.text
            t = t.replace('\'', '"')

            print(f'task add project:evernote \'{t}\'')


def main() -> None:
    read_xml()


if __name__ == '__main__':
    main()
