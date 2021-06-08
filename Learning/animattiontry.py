import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''for i in range(5):
    frame = np.random.randint(0, 256,(1280, 720, 3), dtype=np.uint8)
    plt.title('Try animatiom' + ' ' + str(i))
    plt.xlabel('DCY')
    plt.ylabel('DCX')
    #plt.gcf()
    plt.imshow(frame, origin='lower')
    plt.show()
    plt.clf()
    #plt.pause(0.5)'''

# Usually we use `%matplotlib inline`. However we need `notebook` for the anim to render in the notebook.
# matplotlib notebook


fps = 30
nSeconds = 5
snapshots = [np.random.rand(5, 5) for _ in range(nSeconds * fps)]

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(8, 8))

a = snapshots[0]
im = plt.imshow(a, interpolation='none', aspect='auto', vmin=0, vmax=1)


def animate_func(i):
    if i % fps == 0:
        print('.', end='')
    im.set_array(snapshots[i])
    return [im]


anim = animation.FuncAnimation(fig, animate_func, frames=nSeconds * fps, interval=(1000 / fps))  # in ms

#plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg path on your machine' (e.g.: "C:\FFmpeg\bin\ffmpeg.exe")
anim.save('test_anim.mp4', fps=fps)

print('Done!')
