import numpy
import matplotlib.pyplot as plt

# matrix representaiton of the graph
graph = numpy.array([[0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                     [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                     [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]])

# Part (a)
# row identity
H = []
for row in graph:
    H.append(row / numpy.sum(row))
# print(H)

# Part (b)
d = 0.85
G = numpy.multiply(d, H) + numpy.multiply(1 - d, numpy.full((10, 10), 0.1))


# print(G)

# Part (d)
def converge(G, vk):
    vk1 = []
    acc = 7
    vals = [[], []]
    iteration = 0
    variance = 1 / (10 ** acc)
    while True:
        vk1 = numpy.dot(vk, G)
        vals[0].append(vk1[4])
        vals[1].append(vk1[6])
        iteration += 1
        if (numpy.all((vk1 - vk) <= variance)):
            vk1 = numpy.round(vk1, acc)
            break
        vk = vk1
    return vk1, iteration, vals


v0 = numpy.full(10, 0.1)
vk1, iterations, vals = converge(G, v0)
print("Number of iterations:", iterations)
print("converged values:", vk1)

# Part(e)
d = 0.55
G = numpy.multiply(d, H) + numpy.multiply(1 - d, numpy.full((10, 10), 0.1))
vk1, iteration1, vals1 = converge(G, v0)

print("d=.55", vals1[1])
print("d=.55", vals1[0])
plt.plot(range(iteration1), vals1[1], label="r(P7)", color='orange')
plt.plot(range(iteration1), vals1[0], label="r(P5)", color='blue')
plt.xlabel('x - number')
plt.ylabel('y - rank')
plt.title('Plot of d=0.55')
plt.grid(True)
plt.legend(loc='best')
plt.show()

d = 0.85
G = numpy.multiply(d, H) + numpy.multiply(1 - d, numpy.full((10, 10), 0.1))
vk2, iteration2, vals2 = converge(G, v0)

print("d=.85", vals2[1])
print("d=.85", vals2[0])
plt.plot(range(iteration2), vals2[1], label="r(P7)", color='orange')
plt.plot(range(iteration2), vals2[0], label="r(P5)", color='blue')
plt.xlabel('x - number')
plt.ylabel('y - rank')
plt.title('Plot of d=0.85')
plt.grid(True)
plt.legend(loc='best')
plt.show()
# Part(f)
v01 = [0.05, 0.05, 0.1, 0.1, 0.1, 0.3, 0.05, 0.05, 0, 0.2]
v02 = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0]
v03 = [0, 0.06, 0.04, 0.1, 0.5, 0.1, 0.1, 0, 0.1, 0]
d = 0.85
G = numpy.multiply(d, H) + numpy.multiply(1 - d, numpy.full((10, 10), 0.1))
vk1, iteration1, vals = converge(G, v01)
vk2, iteration2, vals = converge(G, v02)
vk3, iteration3, vals = converge(G, v03)
print("vk1:", vk1, "iterations:", iteration1)
print("vk2:", vk2, "iterations:", iteration2)
print("vk3:", vk3, "iterations:", iteration3)
