# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def get_shared_point(cluster):
    startingSegment = cluster[0]
    start = max(cluster, key=lambda x: x.start)
    end = min(cluster, key=lambda x: x.end)
    for i in range(start.start, end.end + 1):
        if all(i >= e.start and i <= e.end for e in cluster):
            return i


def optimal_points(segments):
    sortedSegments = sorted(segments, key=lambda x: x.start)
    clusters = [[sortedSegments[0]]]
    # write your code here
    for i, s in enumerate(sortedSegments, start=1):
        lastCluster = clusters[-1]
        if all(s.start <= e.end for e in lastCluster):
            clusters[-1].append(s)
        else:
            clusters.append([s])

    points = list(map(get_shared_point, clusters))
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
