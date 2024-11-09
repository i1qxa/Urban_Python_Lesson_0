from fake_math import divide as fake_divide
from true_math import divide as true_divide

args1 = [5, 0]
print(f"Fake Divide({args1}): {fake_divide(*args1)}")
print(f"True Divide({args1}): {true_divide(*args1)}")
args2 = [5, 3]
print(f"Fake Divide({args2}): {fake_divide(*args2)}")
print(f"True Divide({args2}): {true_divide(*args2)}")
