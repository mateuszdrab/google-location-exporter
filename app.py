from locationsharinglib import Service
import jsonpickle, json, sys

# variables cookies_file, google_email set from python command line arguments
cookies_file = sys.argv[1]
google_email = sys.argv[2]

# validate variables and throw error if empty
if not cookies_file:
    raise ValueError("cookies_file is required")
if not google_email:
    raise ValueError("google_email is required")
# throw error if cookies_file does not exist in file system
try:
    with open(cookies_file) as f:
        pass
except FileNotFoundError:
    raise ValueError("cookies_file does not exist")    

# load location service
service = Service(cookies_file=cookies_file, authenticating_account=google_email)

# iterate through persons and print json
for person in service.get_all_people():
    pickled = json.loads(jsonpickle.encode(person, max_depth=1, unpicklable=True))
    pickled.pop('py/object')
    pickled.pop('_logger')

    #rename all keys in pickled to remove leading underscore
    pickled = {k[1:] if k.startswith('_') else k: v for k, v in pickled.items()}

    print(json.dumps(pickled))


