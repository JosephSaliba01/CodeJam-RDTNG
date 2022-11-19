from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl

class QDataset(Dataset):

    def __init__(self, data, tokenizer, source_max_len = 400, target_max_len = 50):
        self.data = data
        self.tokenizer = tokenizer
        self.source_max_len = source_max_len
        self.target_max_len = target_max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        data_row = self.data.iloc[index]

        source_encoding = self.tokenizer(
            data_row["source"],
            max_length=self.source_max_len,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            add_special_tokens=True,
            # additional_special_tokens=["<hl>", "</hl>"],
            return_tensors="pt"
        )

        
        target_encoding = self.tokenizer(
            data_row["target"],
            max_length=self.target_max_len,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            add_special_tokens=True,
            # additional_special_tokens=["<sep>"],
            return_tensors="pt"
        )

        labels = target_encoding["input_ids"]
        labels[labels == 0] = -100

        return dict(
            source=data_row["source"],
            target=data_row["target"],
            input_ids=source_encoding["input_ids"].flatten(),
            attention_mask=source_encoding["attention_mask"].flatten(),
            labels=labels.flatten()
        )

class QDataModule(pl.LightningDataModule):

    def __init__(self, train_df, test_df, tokenizer, batch_size=2, source_max_len=400, target_max_len=50):
        super().__init__()
        self.train_df = train_df
        self.test_df = test_df
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.source_max_len = source_max_len
        self.target_max_len = target_max_len

    def setup(self, stage=None):
        self.train_dataset = QDataset(
            self.train_df,
            self.tokenizer,
            self.source_max_len,
            self.target_max_len
        )

        self.test_dataset = QDataset(
            self.test_df,
            self.tokenizer,
            self.source_max_len,
            self.target_max_len
        )

    def train_dataloader(self):
        return DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=4
        )

    def val_dataloader(self):
        return DataLoader(
            self.test_dataset,
            batch_size=1,
            num_workers=4
        )

    def test_dataloader(self):
        return DataLoader(
            self.test_dataset,
            batch_size=1,
            num_workers=4
        )


    

    