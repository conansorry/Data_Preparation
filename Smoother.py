import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import math

def smoother(res_in):
    res_out = np.zeros(np.shape(res_in))
    for a in range(len(res_in[-1, :])):
        x = res_in[:, a]
        x2 = savgol_filter(x, 91, 7)
        # if( a > 0):
        # plt.plot(x)
        # plt.plot(x2)
        res_out[:, a] = x2.real
    # plt.savefig()

    return res_out

def save_plt(res_in, res_o, plt_p, res_name):
    fig, axi = plt.subplots()

    AA = np.zeros(len(res_in[:, 1]))
    BB = np.zeros(len(res_in[:, 1]))
    for xx in range(len(res_in[:, 1])):
        AA[xx] = math.sqrt(res_o[xx, 1] * res_o[xx, 1] + res_o[xx, 2] * res_o[xx, 2])
        BB[xx] = math.sqrt(res_o[xx, 1] * res_o[xx, 1] + res_o[xx, 2] * res_o[xx, 2])

    axi.plot(res_in[:, 0], AA[:])
    axi.plot(res_in[:, 0], res_in[:, 1])
    axi.plot(res_in[:, 0], res_in[:, 2])

    axi.plot(res_o[:, 0], BB[:], linestyle="dashed")
    axi.plot(res_o[:, 0], res_o[:, 1], linestyle="dashed")
    axi.plot(res_o[:, 0], res_o[:, 2], linestyle="dashed")
    plt.ylim((-1, 1))
    fig.legend(["mag", "re_ori", "im_ori", "re_modi", "im_modi"])

    axi.set_title(res_name)
    fig.savefig(plt_p + res_name + ".png")
    plt.close(fig)



def Smooth():
    res_p = "D:\Dropbox\Python Program\Forward Interpretor\\test\Smooth\\"
    plt_p = "D:\Dropbox\Python Program\Forward Interpretor\\test\Smooth_plt\\"

    for i in range(200):
        print(i)


        res_name = "Res_Smooth_" + str(i)
        res_in = np.loadtxt("D:\Dropbox\Python Program\Forward Interpretor\\test\Res\Res_" + str(i) + ".txt")
        res_o = smoother(res_in)

        np.savetxt(res_p + res_name + ".txt", res_o)

        save_plt(res_in, res_o, plt_p, res_name)





