from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    tags = []
    with open(RSS_FEED) as file:
        for line in file:
            if "-" in line.lower():
                fline = line.replace('-', ' ').lower()
                tags = TAG_HTML.findall(fline)
    # re.findall(r'\w+', open('hamlet.txt').read().lower())
    return tags

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    cnt = Counter()
    for tag in tags:
        cnt[tag] += 1
    return cnt.most_common(10)

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""

    permut = product(list(set(tags)), list(set(tags)))
    a = list(permut)
    similar = []
    for tup in a:
        s = SequenceMatcher(None, tup[0], tup[1])
        ratio = s.ratio()
        if ratio >= SIMILAR and tup[0] != tup[1] and tup[0] != tup[1]+'s':
            similar.append(tup)
    return similar

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
