isRaining = False
print("Today I have the clothes " + ("dry.", "wet.")[isRaining])
print("Today I have the clothes " + ("wet." if isRaining else "dry."))
# [expression] ? A : B
