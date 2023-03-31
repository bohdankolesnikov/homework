# 13.9вг

from mod import *

with open("file.txt", "r") as f:
    pts = [];
    for line in f:
        tmp = line.replace(" ", "").replace("(", "").replace(")", "").replace("\n", "").split(",");
        for i in range(0, len(tmp), 2):
            pts.append(Point(float(tmp[i]), float(tmp[i + 1])));
            
    # в

    max_count = 0;

    max_seg = LineSegment(pts[0], pts[0]);

    for i in range(len(pts)):
        for j in range(i, len(pts)):
            pts_count = 0;
            tmp_seg = LineSegment(pts[i], pts[j]);
            for pt in pts:
                if (tmp_seg.on_segment(pt)):
                    pts_count = pts_count + 1;
            if (pts_count > max_count):
                max_count = pts_count;
                max_seg = tmp_seg;

    max_seg.show();
            
