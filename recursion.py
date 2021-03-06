def all_star(input_string):
  if len(input_string) == 0:
    return ""
  elif len(input_string) == 1:
    return input_string
  else:
    return input_string[0:1] + "*" + all_star(input_string[1:])

print("all_star(\"joshua\") --> " + all_star("joshua") + "\n")


def pair_star(input_string):
  if len(input_string) == 0:
    return ""
  elif len(input_string) == 1:
    return input_string
  elif input_string[0] == input_string[1]:
    return input_string[0] + "*" + pair_star(input_string[1:])
  else:
    return input_string[0] + pair_star(input_string[1:])

print("pair_star(\"jjoosshua\") --> " + pair_star("jjoosshua") + "\n")


def end_x(input_string):
  if len(input_string) == 0:
    return ""
  elif input_string[0] == "x":
    return end_x(input_string[1:]) + "x"
  else:
    return input_string[0] + end_x(input_string[1:])

print("end_x(\"jxxoshxuxax\") --> " + end_x("jxxoshxuxax") + "\n")


def count_pairs(input_string):
  if len(input_string) < 3:
    return 0
  elif input_string[0] == input_string[2]:
    if len(input_string[1:]) > 2:
      return 1 + count_pairs(input_string[1:])
    else:
      return 1
  else:
    return count_pairs(input_string[1:])

print("count_pairs(\"axa\") --> " + str(count_pairs("axa")))
print("count_pairs(\"axax\") --> " + str(count_pairs("axax")))
print("count_pairs(\"axbx\") --> " + str(count_pairs("axbx")) + "\n")


def count_abc(input_string):
  if len(input_string) < 3:
    return 0
  elif input_string[0:3] == "abc" or input_string[0:3] == "aba":
    if len(input_string[1:]) > 2:
      return 1 + count_abc(input_string[1:])
    else:
      return 1
  else:
    return count_abc(input_string[1:])

print("count_abc(\"abc\") --> " + str(count_abc("abc")))
print("count_abc(\"abcxxabc\") --> " + str(count_abc("abcxxabc")))
print("count_abc(\"xabcxabaxx\") --> " + str(count_abc("xabcxabaxx")) + "\n")

def count_11(input_string):
  if len(input_string) < 2:
    return 0
  elif input_string[0:2] == "11":
    if len(input_string[2:]) > 1:
      return 1 + count_11(input_string[2:])
    else:
      return 1
  else:
    return count_11(input_string[1:])

print("count_11(\"11abc11\") --> " + str(count_11("11abc11")))
print("count_11(\"abc11x11x11\") --> " + str(count_11("abc11x11x11")))
print("count_11(\"111\") --> " + str(count_11("111")) + "\n")

def string_clean(input_string):
  if len(input_string) == 1:
    return input_string[0]
  elif input_string[0] == input_string[1]:
    return string_clean(input_string[1:])
  else:
    return input_string[0] + string_clean(input_string[1:])

print("string_clean(\"yyzzza\") --> " + string_clean("yyzzza"))
print("string_clean(\"abbbcdd\") --> " + string_clean("abbbcdd"))
print("string_clean(\"Hello\") --> " + string_clean("Hello") + "\n")

def count_hi2(input_string):
  if len(input_string) == 1:
    return 0
  elif len(input_string) == 2:
    if input_string == "hi":
      return 1
    return 0
  elif len(input_string) > 2:
    if "hi" in input_string[0:3]:
      if input_string[0] == "x":
        return 0 + count_hi2(input_string[2:])
      return 1 + count_hi2(input_string[2:])
    return 0 + count_hi2(input_string[1:])

print("count_hi2(\"ahixhi\") --> " + str(count_hi2("ahixhi")))
print("count_hi2(\"ahibhi\") --> " + str(count_hi2("ahibhi")))
print("count_hi2(\"xhixhi\") --> " + str(count_hi2("xhixhi")) + "\n")
