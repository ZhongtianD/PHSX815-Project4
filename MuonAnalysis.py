
import sys
import numpy as np
import matplotlib.pyplot as plt

# main function for our muon analysis Python code
if __name__ == "__main__":
    

    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH1:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print
        sys.exit(1)
    
    b_SM = 18.10
    sigma_SM = 0.43
    
    #loading files    
    file0 = np.load(InputFile0)
    file1 = np.load(InputFile1)
    Nsample0 = file0.shape[0]
    Nsample1 = file1.shape[0]
    
    #calculate mean and standard error for each experiments
    b_0 = np.mean(file0)
    b_1 = np.mean(file1)
    sigma_0 = np.std(file0)/np.sqrt(Nsample0)
    sigma_1 = np.std(file1)/np.sqrt(Nsample1)
    
    #caculate the combined mean and uncertainty
    b_Exp = (b_1*sigma_0**2+b_0*sigma_1**2)/(sigma_0**2+sigma_1**2)
    sigma_Exp = sigma_0*sigma_1/np.sqrt(sigma_0**2+sigma_1**2)
    
    #calculare significance
    sigma = np.sqrt(sigma_SM**2+sigma_Exp**2)
    Sig = np.abs(b_Exp-b_SM)/sigma
    Sig = np.round_(Sig, decimals=1)

    # make figure
    plt.figure()

    plt.errorbar([b_SM], [1], xerr=[sigma_SM], fmt='o', c='g',label="SM prediction")
    plt.errorbar([b_Exp], [2], xerr=[sigma_Exp], fmt='o', c='m',label="experiment average")
    plt.errorbar([b_0], [3], xerr=[sigma_0], fmt='o', c='r',label="experiment 1")
    plt.errorbar([b_1], [4], xerr=[sigma_1], fmt='o', c='b',label="experiment 2")
    plt.legend()

    ax = plt.gca()
    ax.axes.yaxis.set_ticks([])


    plt.xlabel('$a_\\mu \\times 10^9 -1165900$')
    plt.title(str(Sig)+'$\\sigma$ significance')


    plt.savefig('Muon_measurements.png')
    plt.show()
    
    #print(b_Exp,b_0,b_1,sigma_0,sigma_1)
    
