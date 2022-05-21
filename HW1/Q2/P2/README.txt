This directory contains five files and a directory containing the created flows in addition to this README:
   - create_net.py: creates the topology h1--s1--s3--s2--h2
   - create_flows.py: creates the json files of the flows in seperate directories inside flows-json (s1-flows, s2-flows and s3-flows)
   - del-flows.py: deletes the flows from the controller by sending delete requests
   - push-flows.py: pushes the files created by create_flows.py to the controller by sending put requests containing the jsons
   - Q2_P2_script: This file contains the script of the terminal which shows the steps done and proves that the hosts ping each other in the end.
