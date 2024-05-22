from pathlib import Path
import random

BASE = "shoe/"

# Get all files and seperate them into train, valid, and test as proper ratio (5:3:2)
allfiles = list(Path(BASE).rglob('*.jpg'))
random.shuffle(allfiles)

train = allfiles[:int(len(allfiles)*0.5)]
valid = allfiles[int(len(allfiles)*0.5):int(len(allfiles)*0.8)]
test = allfiles[int(len(allfiles)*0.8):]

Path("train.txt").write_text("\n".join([str(x) for x in train]))
Path("valid.txt").write_text("\n".join([str(x) for x in valid]))
Path("test.txt").write_text("\n".join([str(x) for x in test]))
