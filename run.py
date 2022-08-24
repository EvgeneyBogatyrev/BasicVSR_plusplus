import os

with open("/model/run.sh", "w") as f:
    f.write("cd /model\n")
    f.write("pip3 install -e .\n")

os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")

os.system(f"python3 /model/demo/restoration_video_demo.py /model/configs/basicvsr_plusplus_reds4.py /chkpts/basicvsr_plusplus_reds4.pth /dataset/{video} /results/{video}")
