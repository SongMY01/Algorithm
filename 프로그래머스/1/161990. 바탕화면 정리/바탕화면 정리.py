def solution(wallpaper):
    lux = float('inf')
    luy = float('inf')
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):        # 행
        for j in range(len(wallpaper[0])): # 열
            if wallpaper[i][j] == "#":
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)

    return [lux, luy, rdx, rdy]
