digits = [4,3,2,1]

# approach 1
"""
num = int("".join(map(str, digits))) + 1
print(list(map(int, list(str(num)))))
"""


# the idea is to create an integer which is equal to elements in a array joined individually
"""
4000
 300
  20
+  1
----
4321

We can achieve this by multiplying each nummber with its respective 10s
"""

output = 0
for index, d in enumerate(digits):
    output += d * pow(10, (len(digits)-1)-index)

print(output+1)

# approach 2 -> can solve by recursion

