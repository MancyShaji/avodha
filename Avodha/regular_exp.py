# import re
# pattern = r"avodha"
# if re.match(pattern,"avodha hellow avodha how r u?)"):
#     print("matched")
# else:
#     print("not matched")    

# import re
# pattern = r"y"
# if re.search(pattern,"hello avodha,how r u?"):
#     print("matched")
# else:
#     print("not matched")     

# import re
# pattern = r"a"
# print(re.findall(pattern,"avodhaahjhjgcdgavodhabnjbjyrfdcavodhahfhuf"))

# import re
# str = "hai avodha,how r u?"
# pattern = "avodha"
# new1 = re.sub(pattern,"AVODHA_NEW",str)
# print(new1) 

# import re
# pattern = r"av..dha"
# if re.match(pattern,"avoodha"):
#     print("matched")
# else:
#     print("not matched")    

import re
pattern = r"[A_Z][a-z][0-9]"
if re.search(pattern,"A06"):
    print("correct")
else:
    print("wrong")    