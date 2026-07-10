#
# names = ["ali", "Ahmed", "raza", "sara"]
# print(names)
#
# names_start_with_a = []
# for name in names:
#     name = name.lower()
#     print(name)
#     if name.startswith("a"):
#         if len(name) > 3:
#             names_start_with_a.append(name)
# print(names_start_with_a)
#
# names_start_with_a = [name for name in names if name.lower().startswith("a")]
# print(names_start_with_a)

# ========================================================

name = "Chaudhry IFtikhar HuSSain"
name = name.lower()

if "hussain" in name:
    print("contains")
else:
    print("not contains")

print("contains") if "hussain" in name else print("not contains")
