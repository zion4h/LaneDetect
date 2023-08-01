from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

preprocess = transforms.Compose([
    # transforms.Scale(256),
    # transforms.CenterCrop(224),
    transforms.ToTensor(),
])


def cu_lane_loader(path):
    img_pil = Image.open(path)
    img_pil = img_pil.resize((224, 224))
    img_tensor = preprocess(img_pil)
    return img_tensor


class TrainDataset(Dataset):
    def __init__(self, root_dir, loader=cu_lane_loader):
        # CuLane 原始数据
        self.original_image_width = 1640
        self.original_image_height = 590
        # 需要准备三份数据 图片、分割图、点
        self.images = root_dir + "/data/CuLane"
        self.target = root_dir + "/data/CuLane/Validation"
        self.loader = loader
        return

    def __getitem__(self, idx):
        # 行锚点：一行有anchor_row个
        # 车道线类型： 共 5 种，ll lr rl rr nil
        # 对于一个图像来说，它有 h * anchor_row * num_cls
        # 测试一下
        return None, None

    def __len__(self):
        return 0
