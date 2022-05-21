The directory contains the following files:
    - autorun_net.py: This files should be executed by root. 
        -- It first opens a CLI and gets the network matrix as the input. It also creates the directory 'data' which contains the data that
           is going to be shared between the scripts (these files are the A matrix, the shortest paths and the dictionary that maps the interfaces to their equivalent ports. It worths mentioning
           that these files are stored with json format)
        -- Then it uses the spf.py script in order to calculate the shortest path from 1 to n and vice versa. Then these paths are saved in the directory 'data' with names 'spf_1_n.json' and 
           'spf_n_1.json'. 
        -- Finally the script uses topology() function which is imported from create_net.py and creates the topology and opens the mininet CLI.

    - create_net.py: 
        -- This script creates the topology and also creates a dictionary which maps the name of an interface to it's equivalent port (because ODL takes the port number instead of 
           the interface number)
    
    - spf.py: 
        -- This script uses networkx dijkstra_path() and returns the shortest path from 1 to n and vice versa.
    
    - create_flows.py:
        -- This script creates the json files of the flows and saves them inside the 'flows-json' directory. 
    
    - send_flows.py:
        -- This script should be run with python3.
        -- It uses the requests python module to send put request containing the flows to the controller.
    
    - reset.py:
        -- This script simply clears all the created directories (data, flows-json) and also sends a delete request of the whole opendaylight node inventory 
           which would eventually clear all the flows


The directory contains the following directories:
    - data: contains the files which should be shared between scripts (A, spf_1_n, spf_n_1, port_intf_dict)
    
    - flows-json: contains subdirectories in which the flows of a certain switch is stored. (s#-flows)
