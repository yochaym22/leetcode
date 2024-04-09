# https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150
# TODO need to fix issue with the last row spaces, good enough for now
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_len = len(words[0])
        rows = [
            {'words': [words[0]], 'len': len(words[0])}
        ]
        row_index = 0
        for i in range(1, len(words)):
            if curr_len + len(words[i]) + 1 < maxWidth:
                curr_len += len(words[i]) + 1
                rows[row_index]['words'].append(words[i])
                rows[row_index]['len'] += len(words[i])
            else:
                curr_len = len(words[i])
                row_index += 1
                rows.append({'words': [words[i]], 'len': len(words[i])})

        for i in range(len(rows)):
            spaces = maxWidth - rows[i]['len']
            div = len(rows[i]['words']) - 1 if len(rows[i]['words']) > 1 else 1
            mid_space = spaces // div
            carry = spaces % div
            s = (' ' * mid_space).join(rows[i]['words'])
            rows[i] = s[:len(rows[i]['words'][0])] + ' ' * carry + s[len(rows[i]['words'][0]):]

        return rows



a = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
res = a.fullJustify(words, maxWidth)
for row in res:
    print(row)