import cv2, numpy as np, sys, json
plate, screen, quad, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
P = cv2.imread(plate).astype(np.float32); Sc = cv2.imread(screen).astype(np.float32)
h, w = Sc.shape[:2]
src = np.float32([[0,0],[w,0],[w,h],[0,h]]); dst = np.float32(quad)
M = cv2.getPerspectiveTransform(src, dst)
# soften to the plate's sharpness, a touch of screen brightness
Sc = cv2.GaussianBlur(Sc, (0,0), 1.2) * 0.92 + 8
warp = cv2.warpPerspective(Sc, M, (P.shape[1], P.shape[0]), flags=cv2.INTER_AREA)
m = cv2.warpPerspective(np.ones((h,w),np.float32), M, (P.shape[1], P.shape[0]))
m = cv2.erode(m, np.ones((3,3),np.uint8))
# keep her fingers in front: skin in the ORIGINAL plate inside the quad
ycc = cv2.cvtColor(P.astype(np.uint8), cv2.COLOR_BGR2YCrCb)
skin = ((ycc[...,1] > 138) & (ycc[...,1] < 180) & (ycc[...,2] > 80) & (ycc[...,2] < 130)).astype(np.uint8)
skin = cv2.morphologyEx(skin, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
skin = cv2.dilate(skin, np.ones((3,3),np.uint8)).astype(np.float32)
a = cv2.GaussianBlur(m * (1 - skin), (0,0), 0.8)[...,None]
O = P * (1 - a) + warp * a
# the screen's glow on the hands just around it
glow = cv2.GaussianBlur(warp * m[...,None], (0,0), 18)
O = O + 0.18 * glow * (1 - a)
cv2.imwrite(out, np.clip(O, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
