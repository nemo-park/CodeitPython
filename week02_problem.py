import math

dots = [[(1.0,1.0),(1.0,-1.0),(-1.0,1.0),(-1.0,1.0)],
        [(0.0,2.0),(1.0,0.0),(-1.0,0.0)]]

def getDistance(tuple1, tuple2) -> float:

    # get distance between two dots
    a = tuple2[0] - tuple1[0]
    b = tuple2[1] - tuple1[1]
    return math.sqrt((a*a) + (b*b))

#################

def calcRectangleArea(t) -> float:

    tuple1 = t[0]
    tuple2 = t[1]
    tuple3 = t[2]
    tuple4 = t[3]

    candidate = []
    candidate.append(getDistance(tuple1, tuple2))
    candidate.append(getDistance(tuple1, tuple3))
    candidate.append((getDistance(tuple1, tuple4)))
    # 제일 긴 대각선 제외
    candidate.sort(reverse=True)

    # get width
    width = candidate[1]

    # get height
    height = candidate[2]

    # get area
    return width * height
#################


def calcTriangleArea(t) -> float:

    tuple1 = t[0]
    tuple2 = t[1]
    tuple3 = t[2]

    # get distance of side a
    a = getDistance(tuple1, tuple2)

    # get distance of side b
    b = getDistance(tuple2, tuple3)

    # get distance of side c
    c = getDistance(tuple3, tuple1)

    # get s
    s = (a+b+c)/2

    # get area
    return math.sqrt((s * (s-a) * (s-b) * (s-c)))

#################

def main():

    for i in dots:
        # print dots
        print(i)

        # if there are 3 dots, use calcTriangleArea(t)
        if (len(i) == 3):
            area = calcTriangleArea(i)
        # if there are 4 dots, use calcRectangleArea(t)
        elif (len(i) == 4):
            area = calcRectangleArea(i)

        # print area
        print("면적: {}".format(area))

#################
if __name__ == "__main__":
    main()
