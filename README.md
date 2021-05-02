# PHSX815-Project4

Gaussian_sample.py generates samples drawn from the gaussian distribution using the numpy function.

MuonAnalysis.py creates a plot analyzing two experimental results.

Use the -h flag to see instructions on input parameters.

For example, to generate samples of mu=20.61, use

python Gaussian_sample.py -mu 20.61 -Nsample 10000 -output gaussian1.npy

To analyze simulated samples, use

python MuonAnalysis.py -input0 a_mu0.npy -input1 a_mu1.npy

It will generate a plot showing statistical significance of the experiment.

![alt text](https://github.com/ZhongtianD/PHSX815-Project4/blob/main/Muon_measurements.png?raw=true)
