def solution(sizes):
    answer = 0
    heights = []
    widths = []
    for i, j in sizes:
        heights.append(max(i, j))
        widths.append(min(i, j))
    return max(heights) * max(widths)


solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
