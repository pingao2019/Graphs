d={
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# sum=0
# for k,v in enumerate(d):
#     if type(d[v]) is int:
#         sum+=d[v]
# print(sum)


sum = 0
for value in d.values():
    if type(value) == int:
        sum+=value
print(sum)


# for key  in d:

# for key, value in d.items():
print(d.values())