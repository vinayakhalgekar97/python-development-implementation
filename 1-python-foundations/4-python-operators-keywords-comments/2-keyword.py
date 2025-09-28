import keyword

print(f"Total number of keywords in Python: {len(keyword.kwlist)}")
print(f"Keyword: {", ".join(keyword.kwlist)}")
print(type(keyword.kwlist))