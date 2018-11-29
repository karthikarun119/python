def f():
  print("-- start --")
  yield 3
  print("-- middle --")
  yield 4
  print("-- finished --")
  for v in subgen:
    yield v
gen = f()
next(gen)
next(gen)

subgen = f()

