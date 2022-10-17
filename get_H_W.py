p1 = [58,579]
p2 = [208,758]
p3 = [720,580]
p4 = [520,445]
import numpy as np
import math
def getDist_P2P(Point0,PointA):
    distance=math.pow((Point0[0]-PointA[0]),2) + math.pow((Point0[1]-PointA[1]),2)
    distance=math.sqrt(distance)
    return distance

d14 = getDist_P2P(p1,p4)
d23 = getDist_P2P(p2,p3)
d12 = getDist_P2P(p1,p2)
d34 = getDist_P2P(p3,p4)

max_w = max(int(d14),int(d23))
max_h = max(int(d12),int(d34))

print(max_w,max_h)