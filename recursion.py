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
