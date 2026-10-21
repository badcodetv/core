cd /home/jackt/projects/badcode/badcode/scripts/money-for-something
P="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/images/short7f/m7-ex-close-a.jpg"; V="/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/bank robbery/vids/short7f"
run(){ for t in 1 2 3; do MFS_DURATION=$1 npx tsx mfs-clip.mts "$P" ../bank-robbery/.tmp/$2.txt "$V/$3.mp4" --mode frames 2>&1 | tail -3; [ -f "$V/$3.mp4" ] && return; sleep 10; done; }
run 8 m7-ex-a m7-ex-a1
MFS_SKIP_UPLOAD=1 true
run 8 m7-ex-a m7-ex-a2
run 6 m7-ex-b m7-ex-b1
run 6 m7-ex-b m7-ex-b2
echo ALLDONE
