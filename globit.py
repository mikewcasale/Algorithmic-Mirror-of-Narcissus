import glob
import numpy as np

files = glob.glob('./codedata/*/*', recursive=True)

# Split files into test/train set
np.random.seed(1000)  # For reproducability
np.random.shuffle(files)
N = int(float(len(files))*0.8)  # Do an 80-20 split for training/validation

data = dict(
    train=files[:N],
    valid=files[N-len(files):],
)

num_nq_examples = dict(train=N, valid=len(files)-N)

print(num_nq_examples)

4/xwGvwGvB0IQMLu0Xcf9YrafV36Xw7jCJlOtVgHW9vs2MteSw3Dom-Wc