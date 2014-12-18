#Unit Tests for c302

**_Note: Work in Progress_**

[![Build Status](https://travis-ci.org/ahrasheed/CElegansNeuroML.svg?branch=master)](https://travis-ci.org/ahrasheed/CElegansNeuroML)

##c302_connection_test_A

The script contains two tests and a common setup as described below:

- setUp: Script generates .nml file for each pair in [CElegansNeuronTables.xls](https://github.com/openworm/CElegansNeuroML/blob/master/CElegansNeuronTables.xls) and each pair in from a formatted version of [NeuronConnect.xls](http://www.wormatlas.org/images/NeuronConnect.xls) using the c302 model (c302.py) and SpreadsheetDataReader.py (already in the package and used by c302.py). File for each pair is generated only once.  The script still uses SpreadsheetDataReader.py to read from NeuronConnect, thus Spreadsheet Reader has been modified to accommodate reading NeuronConnect file.

###c302_connection_test
- Test picks each connection pair from CElegansNeuronTables.xls one by one and reads its .nml file using the loader function in libNeuroML. When using parameter_A.py to generate the .nml files, all connection information is encoded in 'projection' components. Hence the test reads the projection components and tests whether the .nml file contains the connection pairing described in the excel file. Right now, it does that by comparing the id (composite of origin, target and synapse type) and synapse (composite of synapse name and number of connections) tags.
- Please note there is only one test being run on all connection pairs. All connection pairs pass this test because the c302 model takes information from the same CElegansNeuronTables.xls in order to build the .nml files. Hence this activity is redundant in the current scenario. It does verify that .nml files being generated by c302 are correct in terms of connections.

###neuronconnect_connection_test
- Test picks connection pairs from NeuronConnectFormatted.xls.
- While CElegansNeuronTables provides detailed classification of chemical synapses, NeuronConnect does not. NeuronConnect does classify Gap Junctions (EJ) from chemical synapses. So the test only checks for connections and does not verify detailed classification of the synapse as with previous test.
- This test catches assertion errors and logs them in an excel file (error_log.xls), thus showing which connection pairs were not present in c302.

##c302_connection_test_B

- This scripts does the same thing as the previous one, but it uses parameters_B.py
- When building .nml files from parameters_B, the connection information for Gap Junctions is stored in 'electricalProjection' components and information for chemical synapses is stored in 'synapticConnection' components. Thus this script treats them separately when conducting the test.

##spreadsheet_comparison_test

- This script does a pair by pair comparison between connections in CElegensNeuronTables.xls and a formatted version of NeuronConnect.xls
- Errors are written to log file (comparison_error_log)

**_SpreadsheetDataReader.py and c302.py have been modified to support the test scripts_**
