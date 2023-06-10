#  ***************************Question 2************************

# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }

#Code

def mapper(extension_type_list, extensions):
    helper = {}
    ans = {}

    extension_pairs = extension_type_list.split(";")
    for pair in extension_pairs:
        extension, file_type = pair.split(",")
        helper[extension] = file_type


    for file_name in extensions:
        file_parts = file_name.split(".")
        if len(file_parts) > 1:
            extension = file_parts[-1]
            if extension in helper:
                ans[file_name] = helper[extension]
            else:
                ans[file_name] = "unknown"
        else:
            ans[file_name] = "unknown"

    return ans


extension_type_list = input("Enter extension and type values: ")
extensions = []
n = int(input("Enter size of list of filenames: "))
for i in range(0, n):
    file = input("Enter the filename: ")
    extensions.append(file)

ans = mapper(extension_type_list, extensions)
print(ans)