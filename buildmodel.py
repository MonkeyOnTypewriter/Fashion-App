
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor

import torch
import torch.utils.data

from SegmentationDataset import SegmentationDataset





def build_model(num_classes):

    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)

    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels

    hidden_layer = 256
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask,
                                                       hidden_layer,
                                                       num_classes)
    
    return model





# defining loss

class_loss = torch.nn.CrossEntropyLoss()
box_loss = torch.nn.SmoothL1Loss()
mask_loss = torchvision.ops.maskrcnn_loss()





# our dataset has two classes only - background and person
num_classes = 2
model = build_model(num_classes)

print('model built success')


#Loading Data


def collate_fn(batch):
    return tuple(zip(*batch))

dataset = torch.load('train.pth')
dataset_test = torch.load('test.pth')

data_loader = torch.utils.data.DataLoader(
    dataset, batch_size=16, shuffle=True,
    collate_fn=collate_fn)

data_loader_test = torch.utils.data.DataLoader(
    dataset_test, batch_size=1, shuffle=False,
    collate_fn=collate_fn)

print('data load success')


#Sending model to Device


device = torch.device('cpu')
model.to(device)

print('model sent to device success')




loss = 


# construct an optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,)

print('optimizer built')



# defining loss function










