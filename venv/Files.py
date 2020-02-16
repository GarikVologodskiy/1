import os
from fnmatch import fnmatch

path = '/Users/igorvologodskiy/PycharmProjects'

name = 'Edu_1.py'
print('Content: ', os.listdir(path))
path_file = []
for root, dirs, files in os.walk(path):
    for f in files:
        if fnmatch(f, name):
            path = (os.path.join(root, f))
            path_file.append(path)

print(path_file)

# def f(path, level=1, name):
#     try:
        # for line in os.listdir(path):
        #     if os.path.isfile(path + '\\' + line):
        #          print('Спускаемся', path + '\\' + line)
    # except:
    #      print('No access')
    # else:
    #      f(path + '\\' + line, level + 1)
    #      print('Возвращаемся в', path)
    # finally:
    #      print('Scanning is over')

# f(path)

# with open('C:\\Users\\student\\Documents\\test.txt', 'r', encoding='utf-8') as inFile:
#     a = []
#     try:
#         for i in inFile:
#             a.append(int(i))
#     except ValueError:
#         print('Not a number')
#     except Exception:
#         print('Not define')
#     else:
#         print('Everything is good')
#     finally:
#         print('File is closed')
#
#
# import os
#
# path = 'C:\\Users\\student\\Documents\\1'
# name = 'test.txt'
#
#
# def f(name, path):
#     for root, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)
#
#         # for line in os.listdir(path):
#         #     if os.path.isfile(path + '\\' + line):
#         #         if name in line:
#
#         # print('Спускаемся', path + '\\' + line)
#     # except:
#     #     print('No access')
#     # else:
#     #     f(path + '\\' + line, level + 1)
#     #     print('Возвращаемся в', path)
#     # finally:
#     #     print('Scanning is over')
#
#
# f(name, path)
#
# import os
# path = 'C:\\Users\\student\\Documents\\1'
#
# def f(path, level=1, name = 'text.txt'):
#      print('Level=', level, 'Content: ', os.listdir(path))
#      for line in os.listdir(path):
#          if os.path.isfile(path + '\\' + line):
#              if name in line:
#                  # return os.path.join(line, name)
#                  return line
#              print('Спускаемся', path + '\\' + line)
#              f(path + '\\' + line, level + 1)
#              print('Возвращаемся в', path)
#
# f(path)