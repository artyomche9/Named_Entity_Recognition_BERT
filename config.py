import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 10
MODEL_PATH = './model'
TRAINING_FILE = "./data/ner_datasetreference.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
