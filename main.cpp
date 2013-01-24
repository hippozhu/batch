#include "mycommon.h"
#include "SVMData.h"
#include "Neighborhood.h"
#include "KernelNeighborhood.h"
#include "Solver.h"

int main(int argc, char** argv){
  string filestem(argv[1]);
  //int NFeature = atoi(argv[2]);
  int NClass = atoi(argv[2]);
  int k = atoi(argv[3]);
  double mu = atof(argv[4]);
  double alpha = atof(argv[5]);
  
  SVMData data_train(filestem+".train"); 
  SVMData data_test(filestem+".test");
  cout << "a1" << endl;
  KernelNeighborhood nb(data_train, data_test, NClass, k);
  //cout << "t: " << nb.target[0] << " " << nb.target[1] << " " << nb.target[2] << endl;
  cout << nb.nfeat << "*" << nb.ninst << ", k=" << nb.k << endl;  
  Solver s(nb, mu, alpha);
  double *r = (double *)malloc(sizeof(double) * nb.nfeat * nb.ninst);
  kernelTest(nb.nfeat, nb.ninst, nb.ninst_test, nb.k, r, s.alpha);
  //s.cusolve();
}

