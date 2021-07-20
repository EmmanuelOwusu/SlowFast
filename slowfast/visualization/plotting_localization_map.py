import numpy
import matplotlib.pyplot as plt
from slowfast.visualization.gradcam_utils import *
import imageio
import cv2



from pathlib import Path
path = Path('/mnt/data/ni/ahenkan/SlowFast')
path.mkdir(parents=True, exist_ok=True)


###Loading the localization maps
#load_localization_map = numpy.load(path/f'localization_map_ClassB_0_140349810510912.npy')
#print(load_localization_map)
#load_localization_map = load_localization_map.squeeze()
#plt.show(load_localization_map)

#print(load_localization_map.shape)
# plt.plot(load_localization_map)
# cv2.imread('load_localization_map')
# cv2.imshow

# cap = cv2.VideoCapture('load_localization_map')
# while(cap.isOpened()):
#   ret, frame = cap.read()
#   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   cv2.imshow('frame',gray)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# cap.release()
# cv2.destroyAllWindows()


### Loading the data
with open("/mnt/data/ni/ahenkan/SlowFast/complete_locmap_input.pkl","rb") as fb:
    output =pickle.load(fb)

print(len(output))

####PLOTTING THE LOCALIZATION MAPS ON TOP OF THE INPUT CLIPS
#for dict1 in output:
D = output[0]
    
     
for i in range(len(output)):
    print(output[i]["ClassA"].keys)




# #### Reading the Videos
# vid = imageio.get_reader(f'/mnt/data/ni/ahenkan/SlowFast/configs/MyData/ClassA/play.mp4','ffmpeg')
# vidlist = []
# for image in vid.iter_data():
#     vidlist.append(numpy.array(image))
# #print(numpy.array(image).shape)
# #print(len(vidlist))

