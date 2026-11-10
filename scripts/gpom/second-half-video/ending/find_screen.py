import cv2, numpy as np, sys
# find the bright phone screen quad in a plate, within a search box
img = cv2.imread(sys.argv[1]); x0,y0,x1,y1 = map(int, sys.argv[2].split(','))
roi = img[y0:y1, x0:x1]; g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(g, int(sys.argv[3]) if len(sys.argv)>3 else 120, 255, cv2.THRESH_BINARY)
th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, np.ones((9,9),np.uint8))
cs,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = max(cs, key=cv2.contourArea); hull = cv2.convexHull(c)
peri = cv2.arcLength(hull, True)
for eps in np.linspace(0.01,0.1,40):
    ap = cv2.approxPolyDP(hull, eps*peri, True)
    if len(ap)==4: break
pts = ap.reshape(-1,2) + [x0,y0]
print(len(ap), cv2.contourArea(c), pts.tolist())
vis = img.copy(); cv2.polylines(vis,[pts.astype(np.int32)],True,(0,0,255),2)
cv2.imwrite(sys.argv[4] if len(sys.argv)>4 else '/dev/null', vis[y0-40:y1+40, x0-40:x1+40])
