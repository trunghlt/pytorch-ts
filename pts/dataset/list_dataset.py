from typing import Iterable
import random

from .common import DataEntry, Dataset, SourceContext
from .process import ProcessDataEntry


class ListDataset(Dataset):
    def __init__(
        self,
        data_iter: Iterable[DataEntry],
        freq: str,
        one_dim_target: bool = True,
        is_train: bool = True,
    ) -> None:
        process = ProcessDataEntry(freq, one_dim_target)
        self.list_data = [process(data) for data in data_iter]
        if is_train:
            random.shuffle(self.list_data)


    def __iter__(self):
        source_name = "list_data"
        for row_number, data in enumerate(self.list_data, start=1):
            data["source"] = SourceContext(source=source_name, row=row_number)
            yield data

    def __len__(self):
        return len(self.list_data)
