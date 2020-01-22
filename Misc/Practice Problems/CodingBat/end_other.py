def end_other(a, b):
  a, b = a.lower(), b.lower()
  return a[-1] == b[-1] and a.count(b) > 0 or a[-1] == b[-1] and b.count(a) > 0
