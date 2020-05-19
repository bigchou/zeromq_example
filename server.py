import zmq, time, torch, os, PIL, pdb, json
from torchvision import transforms, models, datasets

#download the pre-trained weight to the model folder
os.environ['TORCH_HOME'] = 'model'

# define preprocessing
input_size = (224,224)
preprocessing = transforms.Compose([
	transforms.Resize(input_size),
	transforms.ToTensor(),
	transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225]),
])

# prepare model
mobilenet = models.mobilenet_v2(pretrained=True)
mobilenet.eval()
# Load Imagenet Synsets (the following script is based on this repo. https://github.com/Cadene/pretrained-models.pytorch/blob/master/examples/imagenet_logits.py)
with open('imagenet_synsets.txt', 'r') as f:
	synsets = f.readlines()
synsets = [x.strip() for x in synsets]
splits = [line.split(' ') for line in synsets]
key_to_classname = {spl[0]:' '.join(spl[1:]) for spl in splits}
with open('imagenet_classes.txt', 'r') as f:
	class_id_to_key = f.readlines()
	class_id_to_key = [x.strip() for x in class_id_to_key]


print("START SERVER")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
	#  Wait for next request from client
	#[STRING BASED]
	#message = socket.recv()
	#print("Received request: %s" % message)

	#[JSON BASED]
	message = socket.recv_json()
	print("Received request: %s" % message["imgpath"])

	#  Do some 'work'
	if message:
		print("make an inference ...")
		out = None
		with torch.no_grad():
			#img_name = message
			img_name = message["imgpath"]
			sample = PIL.Image.open(img_name).convert("RGB")
			sample = preprocessing(sample)
			sample = sample.unsqueeze(0)#(1,3,224,224)
			output = mobilenet(sample)
			max, argmax = output.data.squeeze().max(0)
			class_id = argmax.item()
			class_key = class_id_to_key[class_id]
			classname = key_to_classname[class_key]
			out = "%s is a %s"%(img_name, classname)
		print(out)

		#  Send reply back to client
		# [STRING BASED]
		#socket.send(str(out).encode())#require btye object instead of str

		# [JSON BASED]
		item = {"out":out}
		item = json.dumps(item)#dict to str
		item_json = json.loads(item)#str to dict
		socket.send_json(item_json)
