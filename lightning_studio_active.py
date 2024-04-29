#! pip install lightning-sdk
import os
from lightning_sdk import Studio

# run from inside a Studio: control the studio you are running on
# s = Studio()
# s.stop()

# Retrieve values from GitHub Secrets
studio_name = os.environ['LIGHTNING_STUDIO_NAME']
teamspace = os.environ['LIGHTNING_TEAMSPACE']
user = os.environ['LIGHTNING_USER']

# Create a new Studio instance with secrets
s = Studio(name=studio_name, teamspace=teamspace, user=user, create_ok=True)
# before we call start, the Studio exists but isn't running
s.start()
output1 = s.run("ls")
print(output1)
# output2 = s.run("python3 main.py")
print(output2)
