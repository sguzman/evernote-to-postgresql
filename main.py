from typing import Optional
from typing import List
from typing import Tuple
import xml.etree.ElementTree as ET

path: str = './notes.enex'


def read_xml() -> List[Tuple[str, str]]:
    tree: ET = ET.parse(path)
    root: ET.ElementTree = tree.getroot()

    title: List[str] = []
    date: List[str] = []

    for child in root.getiterator():
        if child.tag == 'title':
            t: str = child.text
            title.append(t)
        elif child.tag == 'created':
            d: str = child.text

            year: str = d[:4]
            month: str = d[4:6]
            day: str = d[6:8]

            hour: str = d[9:11]
            minutes: str = d[11:13]
            seconds: str = d[13:15]

            full_date: str = f'{year}-{month}-{day}T{hour}:{minutes}:{seconds}'
            date.append(full_date)

    return list(zip(title, date))


def main() -> None:
    extract: List[Tuple[str, str]] = read_xml()
    for e in extract:
        print(f'git commit --date=\'{e[1]}\' --message=\'{e[0]}\' --allow-empty')


if __name__ == '__main__':
    main()
