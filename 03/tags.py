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
    tags = TAG_HTML.findall(open(RSS_FEED).read().lower().replace('-',' '))

    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""

    top_tags = Counter(tags).most_common(TOP_NUMBER)
    return top_tags


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    d = []
    tags = [str(tag) for tag in tags]
    for tag1, tag2 in product(tags, tags):
        if (tag1 != tag2) and (tag1[0] == tag2[0]):
            seq = SequenceMatcher(None, tag1, tag2)
            ratio = seq.ratio()
            if ratio > SIMILAR:
                d.append(sorted((tag1, tag2)))
    d = d[:(len(d))//4]
    return d

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print(get_similarities(tags))
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
