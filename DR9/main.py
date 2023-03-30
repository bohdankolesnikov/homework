# 15.11

def foo(st):
    if (type(st) != str):
        raise TypeError;
    lst = st.split(" ");
    max_size = max(list(map(len, lst)));
    result = [];
    for word in lst:
        if len(word) == max_size:
            result.append(word);

    return list(set(result));

print(foo("Tempore porro sit porro ipsa repellendus quae Tempore porro sit porro ipsa repellendus quae harum. harum."));

print(foo(123));
