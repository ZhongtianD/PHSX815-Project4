
import sys
import numpy as np


sys.path.append(".")
from Random import Gaussian

# main function for our coin toss Python code
if __name__ == "__main__":

    # default seed
    seed = 2048

    # default mean of the distribution
    mu = 20.61
    
    # default deviation of the distribution
    sigma = 41
    

    # default number of samples (per experiment)
    Nsample = 10000

    # output file defaults
    doOutputFile = False

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -seed [number] seed for random number generation")
        print ("   -mu [number] mean for the gaussian distribution")
        print ("   -sigma [number] standard deviation for the gaussian distribution")
        print ("   -Nsample [number] number of samples")
        print ("   -output [.npy file] output file saved in the .npy format")
        print
        sys.exit(1)
    
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mu' in sys.argv:
        p = sys.argv.index('-mu')
        mu = float(sys.argv[p+1])
    if '-sigma' in sys.argv:
        p = sys.argv.index('-sigma')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma = ptemp
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 10:
            Nsample = Ns
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # Initialze an object of the Gaussian class
    G = Gaussian(seed =seed, mu=mu, sigma =sigma)

    if doOutputFile:
        #Generate samples
        print(mu)
        S = G.Gaussian_sample(mu,Nsample)
        np.save(OutputFileName, S)
   
