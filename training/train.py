from dataset import QDataModule
from model import QModel
from sklearn.model_selection import train_test_split
import pandas as pd
import pytorch_lightning as pl
from transformers import T5Tokenizer, logging

MODEL_NAME = "t5-base"
DATASET_PATH = "dataset/train.csv"
LEARNING_RATE = 1e-4
BATCH_SIZE = 2
EPOCHS = 3

def train():
    logging.set_verbosity_error()
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    tokenizer.add_special_tokens({"additional_special_tokens": ["<hl>", "</hl>", "<sep>"]})

    # Load the dataset
    print("Loading dataset...")
    df = pd.read_csv(DATASET_PATH)
    df = df.applymap(str)
    train_df, val_df = train_test_split(df, test_size=0.1) # 10% of the dataset will be used for validation
    data_module = QDataModule(train_df, val_df, tokenizer, batch_size=BATCH_SIZE)
    data_module.setup()

    # Load the model
    print("Loading model...")
    model = QModel(MODEL_NAME, LEARNING_RATE)
    # model.resize_token_embeddings(len(tokenizer))

    checkpoint_callback = pl.callbacks.ModelCheckpoint(
        dirpath="checkpoints",
        filename="best-checkpoint",
        save_top_k=1,
        verbose=True,
        monitor="val_loss",
        mode="min"
    )

    # Train the model
    print("Training model...")

    logger = pl.loggers.TensorBoardLogger("lightning-logs")
    trainer = pl.Trainer(
        logger=logger,
        callbacks=[checkpoint_callback],
        max_epochs=EPOCHS,
        gpus=1
    )

    trainer.fit(model, data_module)
    # trainer.test()

if __name__ == "__main__":
    train()