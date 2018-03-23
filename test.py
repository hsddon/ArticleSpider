list1 = ["abc","1",123,45,"abc1"]


import re
match_list1 = re.search(".*(\d+)","qbc123")
print(match_list1.group()[1])