with open("MAP.INP", "r") as f:
    path = list(f.read().strip())
out_x = lambda x: "E" * x if x < 0 else "W" * x
out_y = lambda y: "N" * y if y < 0 else "S" * y
delta_x = path.count("E") - path.count("W")
delta_y = path.count("N") - path.count("S")
with open("MAP.OUT", "w") as f:
    f.write(out_x(delta_x))
    f.write(out_y(delta_y))
