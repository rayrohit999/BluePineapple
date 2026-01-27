import re
def split_string(string : str, delemeter : str) -> list[str] | None:
    if not delemeter:
        return None
    if not string:
        return []
    regex = "["+delemeter+"]"
    return re.split(regex,string)

print(split_string("banana,apple,rohit!mohit|aniket.cow",",!|."))
print(split_string("banana,apple,rohit!mohit|aniket.cow",""))
print(split_string("",",!|."))

