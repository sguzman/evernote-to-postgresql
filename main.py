from typing import Optional
from typing import List
import xml.etree.ElementTree as ET

path: str = './notes.enex'


def read_xml() -> List[str]:
    tree: ET = ET.parse(path)
    root: ET.ElementTree = tree.getroot()

    items: List[str] = []
    for child in root.getiterator():
        print(child.tag, child.attrib)
        if child.tag == 'title':
            print(child.text.encode('utf8'))

    return items


def main() -> None:
    read_xml()


if __name__ == '__main__':
    main()
